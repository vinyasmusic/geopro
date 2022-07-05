from django.contrib.gis.db import models

from geopro.utils.common_models import GeoProBaseModel


class CountryGeo(GeoProBaseModel):

    iso_code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=200)
    data = models.MultiPolygonField()

    def __str__(self):
        return f"{self.name} {self.iso_code}"
