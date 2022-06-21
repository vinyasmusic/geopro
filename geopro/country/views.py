from typing import Any

from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from geopro.country.models import CountryGeo
from geopro.country.serializers import CountryGeoSerializer


class CountryGeoViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """
    Country Geo
    ---

    """

    serializer_class = CountryGeoSerializer
    queryset = CountryGeo.objects.all()
    lookup_field = "iso_code__iexact"
    search_fields = ["name", "data"]
    geometry_filter_field = "data"

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Search
        ----
        parameters:
        - name: name
          description: Country name
          required: false
          type: string
        - name: polygon
          required: false
        """
        queryset = self.get_queryset()
        if name := request.query_params.get("name"):
            queryset = queryset.filter(name__icontains=name)
        if polygon := request.query_params.get("polygon"):
            queryset = queryset.filter(data__intersects=polygon)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
