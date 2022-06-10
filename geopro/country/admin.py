from django.contrib import admin

from geopro.country.models import CountryGeo


class CountryGeoAdmin(admin.ModelAdmin):
    pass


admin.site.register(CountryGeo, CountryGeoAdmin)
