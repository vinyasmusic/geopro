import logging

import requests

from config import celery_app
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
    country_wise_data = []
    for response_datum in response_data["features"]:
        country_wise_data.append(
            {
                "name": response_datum["properties"]["ADMIN"],
                "iso_code": response_datum["properties"]["ISO_A3"],
                "data": response_datum["geometry"],
            }
        )

    country_serializers = CountryGeoSerializer(data=country_wise_data, many=True)
    if country_serializers.is_valid():
        country_serializers.save()
    else:
        logger.error(country_serializers.errors)
