from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CountryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "geopro.country"
    verbose_name = _("Country")

    def ready(self):
        try:
            import geopro.country.signals  # noqa F401
        except ImportError:
            pass
