import json
import logging
from collections import defaultdict

import requests
from django.contrib.gis import geos

from config import celery_app
from geopro.country.models import CountryGeo
from geopro.country.serializers import CountryGeoSerializer

logger = logging.getLogger(__name__)


@celery_app.task(soft_time_limit=300)
def fetch_country_geojson():
    """Fetch data from datahub
    Use requests to get geojson data and publish that data for other workers to
    pick up
    """
    response = requests.get("https://datahub.io/core/geo-countries/r/countries.geojson")
    if not response.ok:
        logger.error("No data found from API", exc_info=True)
        return

    response_data = response.json()
    country_wise_data = defaultdict(dict)
    for response_datum in response_data["features"]:
        country_wise_data[response_datum["properties"]["ISO_A3"]] = {
            "name": response_datum["properties"]["ADMIN"],
            "iso_code": response_datum["properties"]["ISO_A3"],
            "data": response_datum["geometry"],
        }

    existing_countries = CountryGeo.objects.filter(
        iso_code__in=list(country_wise_data.keys())
    )

    for existing_country in existing_countries:
        if isinstance(
            geos.GEOSGeometry(
                json.dumps(country_wise_data[existing_country.iso_code]["data"])
            ),
            geos.Polygon,
        ):
            existing_country.data = geos.MultiPolygon(
                geos.GEOSGeometry(
                    json.dumps(country_wise_data[existing_country.iso_code]["data"])
                )
            )
        else:
            existing_country.data = geos.GEOSGeometry(
                json.dumps(country_wise_data[existing_country.iso_code]["data"])
            )
        country_wise_data.pop(existing_country.iso_code, None)

    CountryGeo.objects.bulk_update(existing_countries, fields=["data"])

    # Whatever is left in country_wise_data is data that is either new or has been deleted
    country_serializers = CountryGeoSerializer(
        data=[v for k, v in country_wise_data.items()], many=True
    )
    if country_serializers.is_valid():
        country_serializers.save()
    else:
        logger.error(country_serializers.errors)
