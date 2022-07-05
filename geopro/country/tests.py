import json

import pytest
from django.contrib.gis import geos
from rest_framework.test import APIRequestFactory, force_authenticate

from geopro.country.models import CountryGeo
from geopro.country.views import CountryGeoViewSet
from geopro.users.models import User

pytestmark = pytest.mark.django_db

SAN_MARINO = {
    "type": "Polygon",
    "coordinates": [
        [
            [12.4294503590001, 43.89205551500001],
            [12.399581381000075, 43.903217625000138],
            [12.385628745000105, 43.924534153000138],
            [12.395653973000037, 43.948408664000027],
            [12.411048669000138, 43.959661012000055],
            [12.421388836000119, 43.967218885000136],
            [12.453324871000092, 43.979052789000065],
            [12.482160321000038, 43.982566786000092],
            [12.489188315000121, 43.973109999000144],
            [12.492392254000094, 43.95641851100001],
            [12.490325196000128, 43.939158583000108],
            [12.48309447400004, 43.929204898000052],
            [12.482160321000038, 43.927918959000067],
            [12.479576499000132, 43.925800225000074],
            [12.478026206000095, 43.923216404000073],
            [12.477493853000112, 43.920050984000085],
            [12.478286774000082, 43.917037885000099],
            [12.460456219000037, 43.895259454000097],
            [12.4294503590001, 43.89205551500001],
        ]
    ],
}


@pytest.fixture
def singapore(db) -> CountryGeo:
    data = json.dumps(
        {
            "type": "Polygon",
            "coordinates": [
                [
                    [103.96078535200013, 1.39109935100015],
                    [103.98568769600007, 1.38544342700007],
                    [103.99952233200003, 1.38031647300005],
                    [104.00342858200003, 1.374172268000066],
                    [103.99187259200011, 1.354925848000036],
                    [103.97486412900014, 1.334458726000065],
                    [103.95435631600009, 1.318101304000052],
                    [103.93189537900008, 1.311468817000076],
                    [103.90723717500009, 1.308742580000114],
                    [103.88770592500003, 1.301255601000136],
                    [103.85271243600005, 1.277289130000085],
                    [103.84693444100009, 1.271918036000045],
                    [103.84408613400012, 1.268500067000034],
                    [103.83887780000003, 1.266262111000046],
                    [103.82601972700007, 1.264308986000089],
                    [103.80160566500007, 1.264797268000081],
                    [103.78956139400003, 1.26788971600007],
                    [103.78443444100003, 1.273871161000088],
                    [103.77588951900009, 1.287583726000108],
                    [103.75513756600003, 1.297105210000012],
                    [103.73015384200011, 1.302923895000063],
                    [103.70875084700003, 1.305243231000119],
                    [103.66529381600009, 1.304103908000087],
                    [103.6476343110001, 1.308417059000092],
                    [103.64039147200003, 1.322251695000091],
                    [103.64470462300005, 1.338039455000043],
                    [103.67457116000003, 1.38031647300005],
                    [103.67888431100005, 1.399237372000073],
                    [103.68384850400008, 1.40989817900001],
                    [103.69507897200009, 1.421332098000065],
                    [103.70834394600013, 1.429388739000089],
                    [103.7179468110001, 1.430975653000118],
                    [103.73975670700008, 1.428127346000082],
                    [103.76221764400009, 1.430975653000118],
                    [103.79004967500003, 1.444281317000048],
                    [103.80494225400008, 1.448635158000045],
                    [103.83155358200003, 1.447088934000092],
                    [103.85718834700009, 1.438706773000135],
                    [103.93246504000007, 1.401109117000132],
                    [103.96078535200013, 1.39109935100015],
                ]
            ],
        }
    )
    data = geos.MultiPolygon(geos.GEOSGeometry(data))
    return CountryGeo.objects.create(name="Singapore", iso_code="SGP", data=data)


@pytest.fixture
def aruba(db) -> CountryGeo:
    data = json.dumps(
        {
            "type": "Polygon",
            "coordinates": [
                [
                    [-69.996937628999916, 12.577582098000036],
                    [-69.936390753999945, 12.531724351000051],
                    [-69.924672003999945, 12.519232489000046],
                    [-69.915760870999918, 12.497015692000076],
                    [-69.880197719999842, 12.453558661000045],
                    [-69.876820441999939, 12.427394924000097],
                    [-69.888091600999928, 12.417669989000046],
                    [-69.908802863999938, 12.417792059000107],
                    [-69.930531378999888, 12.425970770000035],
                    [-69.945139126999919, 12.44037506700009],
                    [-69.924672003999945, 12.44037506700009],
                    [-69.924672003999945, 12.447211005000014],
                    [-69.958566860999923, 12.463202216000099],
                    [-70.027658657999922, 12.522935289000088],
                    [-70.048085089999887, 12.531154690000079],
                    [-70.058094855999883, 12.537176825000088],
                    [-70.062408006999874, 12.546820380000057],
                    [-70.060373501999948, 12.556952216000113],
                    [-70.051096157999893, 12.574042059000064],
                    [-70.048736131999931, 12.583726304000024],
                    [-70.052642381999931, 12.600002346000053],
                    [-70.059641079999921, 12.614243882000054],
                    [-70.061105923999975, 12.625392971000068],
                    [-70.048736131999931, 12.632147528000104],
                    [-70.00715084499987, 12.5855166690001],
                    [-69.996937628999916, 12.577582098000036],
                ]
            ],
        }
    )
    data = geos.MultiPolygon(geos.GEOSGeometry(data))
    return CountryGeo.objects.create(name="Aruba", iso_code="ARW", data=data)


def test_get_country_by_name_200(singapore, user: User, rf: APIRequestFactory):
    request = rf.get("/api/country?name=Sing")
    force_authenticate(request, user)
    view = CountryGeoViewSet.as_view({"get": "list"})
    response = view(request)
    assert response.status_code == 200
    assert response.data["results"]["features"][0]["properties"]["iso_code"] == "SGP"


def test_get_country_by_name_empty(singapore, user: User, rf: APIRequestFactory):
    request = rf.get("/api/country?name=aruba")
    force_authenticate(request, user)
    view = CountryGeoViewSet.as_view({"get": "list"})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data["results"]["features"]) == 0


def test_create_new_country_403(rf: APIRequestFactory):
    # Since there is no authenticated user, API will throw forbidden
    request = rf.post(
        "/api/country/",
        {"name": "India", "iso_code": "IND", "data": json.dumps({"test": "test"})},
    )
    view = CountryGeoViewSet.as_view({"post": "create"})
    response = view(request)
    assert response.status_code == 403


def test_create_new_country_200(user: User, rf: APIRequestFactory):
    data = json.dumps(SAN_MARINO)
    request = rf.post(
        "/api/country/", {"name": "San Marino", "iso_code": "SMR", "data": data}
    )
    view = CountryGeoViewSet.as_view({"post": "create"})
    force_authenticate(request, user)
    response = view(request)
    assert response.status_code == 201


def test_delete_country_not_found(user: User, rf: APIRequestFactory):
    request = rf.delete(
        "/api/country/",
    )
    view = CountryGeoViewSet.as_view({"delete": "destroy"})
    force_authenticate(request, user)
    response = view(request, iso_code__iexact="ARW")
    assert response.status_code == 404


def test_delete_country(singapore, user: User, rf: APIRequestFactory):
    request = rf.delete(
        "/api/country/",
    )
    view = CountryGeoViewSet.as_view({"delete": "destroy"})
    force_authenticate(request, user)
    response = view(request, iso_code__iexact="SGP")
    assert response.status_code == 204


def test_search_by_geometry(
    singapore: CountryGeo, aruba: CountryGeo, user: User, rf: APIRequestFactory
):
    # Searching with San Marino data should not return any result
    data = geos.GEOSGeometry(json.dumps(SAN_MARINO))
    request = rf.get(f"/api/country?geom={data}")
    force_authenticate(request, user)
    view = CountryGeoViewSet.as_view({"get": "list"})
    response = view(request)
    assert response.status_code == 200
    assert len(response.data["results"]["features"]) == 0

    # Searching with singapore data should return result
    data = geos.GEOSGeometry(singapore.data)
    request = rf.get(f"/api/country?geom={data}")
    force_authenticate(request, user)
    response = view(request)
    assert response.status_code == 200
    assert len(response.data["results"]["features"]) == 1
