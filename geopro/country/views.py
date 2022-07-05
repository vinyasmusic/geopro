from typing import Any

from django.contrib.gis.geos import MultiPolygon, Polygon, fromstr
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
    queryset = CountryGeo.objects.all().order_by("name")
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
            queryset = queryset.filter(name__istartswith=name)
        if geom := request.query_params.get("geom"):
            spatial_data = fromstr(geom)
            if isinstance(spatial_data, Polygon):
                geom = MultiPolygon(spatial_data)
            queryset = queryset.filter(data__intersects=geom)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
