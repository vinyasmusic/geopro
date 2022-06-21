from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from geopro.country.views import CountryGeoViewSet
from geopro.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("country", CountryGeoViewSet)


app_name = "api"
urlpatterns = router.urls
