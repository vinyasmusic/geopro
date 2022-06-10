from rest_framework_gis.serializers import GeoFeatureModelSerializer

from geopro.country.models import CountryGeo


class CountryGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CountryGeo
        geo_field = "data"
        fields = ("uuid", "name", "iso_code", "data")
