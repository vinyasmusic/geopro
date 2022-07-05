from django.contrib.gis import geos
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from geopro.country.models import CountryGeo


class CountryGeoSerializer(GeoFeatureModelSerializer):
    def create(self, validated_data):
        if isinstance(validated_data["data"], geos.Polygon):
            validated_data["data"] = geos.MultiPolygon(validated_data["data"])

        return super().create(validated_data)

    class Meta:
        model = CountryGeo
        geo_field = "data"
        fields = ("uuid", "name", "iso_code", "data")
