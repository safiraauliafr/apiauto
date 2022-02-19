from msilib.schema import Class
import requests
# import pytest
from assertpy import assert_that

class Test_airport:

    def test_getAllResponse(self):

        response = requests.get("https://airportgap.dev-tester.com/api/airports/")
        # assert response.status_code != 200
        # pprint(responseFetch.json())
        # assert_that(response.status_code).is_not_equal_to(200)
        assert_that(response.status_code).is_equal_to(200)
        data = response.json().get("data")
        assert_that(data).is_not_empty()
        
    def test_getDetails(self):
        airportId = "CGK"
        response = requests.get(f"https://airportgap.dev-tester.com/api/airports/{airportId}")
        assert_that(response.status_code).is_equal_to(200)
        data = response.json().get("data")
        assert_that(data["attributes"]["name"]).is_equal_to("Soekarno-Hatta International Airport")
        assert_that(data.get("attributes").get("city")).is_equal_to("Jakarta")

    def test_getNotFound(self):
        airportId = "JKT"
        response = requests.get(f"https://airportgap.dev-tester.com/api/airports/{airportId}")
        assert_that(response.status_code).is_equal_to(404)        
        assert_that(response.json()).contains_key("errors")
        assert_that(response.text).contains("The page you requested could not be found")


class Test_airportDistance:

    def test_getCalculateDistance(self):
        airport = {
            "from" : "CGK",
            "to"   : "NRT"
        }
        response = requests.post("https://airportgap.dev-tester.com/api/airports/distance", data = airport)
        assert_that(response.status_code).is_equal_to(200)
        data = response.json().get("data")
        assert_that(data).is_not_empty()
        assert_that(data["id"]).is_equal_to("CGK-NRT")
        assert_that(data["attributes"]["from_airport"]["id"]).is_equal_to(2501)
        assert_that(data["attributes"]["kilometers"]).is_equal_to(5838.929627700195)
        assert_that(data["attributes"]["miles"]).is_equal_to(3625.616952940193)
        assert_that(data["attributes"]["nautical_miles"]).is_equal_to(3150.5734831507266)

    def test_invalidCalculation(self):
        airport = {
            "from" : "CGK",
            "to"   : "JKT"
        }
        response = requests.post("https://airportgap.dev-tester.com/api/airports/distance", data = airport)
        assert_that(response.status_code).is_equal_to(422)
        assert_that(response.json()).contains_key("errors")
        assert_that(response.text).contains("Unable to process request")