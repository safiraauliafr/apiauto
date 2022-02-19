from urllib import response
import requests
from assertpy import assert_that

class Test_post:
    Auth = {"Authorization": "Bearer token=LykwagUbJxiBA2KPZgQBjFeb"}
    URL = "https://airportgap.dev-tester.com/api/favorites"

    def test_postFavorite(self):
        response = requests.post(self.URL, data = {
            "airport_id" : "LAE",
            "note" : "Created at 03/02/2022"
        }, headers = self.Auth)

        assert_that(response.status_code).is_equal_to(201)
        airport = response.json()["data"]["attributes"]["airport"]
        assert_that(airport["name"]).is_equal_to("Wewak International Airport") 
        assert_that(airport["country"]).is_equal_to_ignoring_case("Papua New Guinea") 
        print(response.text)

class Test_get:
    Auth = {"Authorization": "Bearer token=LykwagUbJxiBA2KPZgQBjFeb"}
    URL = "https://airportgap.dev-tester.com/api/favorites"

    def test_getFavorite(self):
        response = requests.get(self.URL, headers = self.Auth)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json().get("data"))).is_greater_than_or_equal_to(1)
        print(response.text)

class Test_update:
    Auth = {"Authorization": "Bearer token=LykwagUbJxiBA2KPZgQBjFeb"}
    URL = "https://airportgap.dev-tester.com/api/favorites"

    def _get_first_favorite(self):
        response_id = requests.get(self.URL, headers = self.Auth)
        return response_id.json().get("data")[0].get("id")

    def test_updateNotes(self):
        id = self._get_first_favorite()
        response = requests.patch(f"{self.URL}/{id}", 
                    headers = self.Auth, data = {
                        "note" : "Updated at now: 19/02/2022"
                    })
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()["data"]["attributes"]["note"]).is_equal_to("Updated at now: 19/02/2022")

class Test_delete:
    Auth = {"Authorization": "Bearer token=LykwagUbJxiBA2KPZgQBjFeb"}
    URL = "https://airportgap.dev-tester.com/api/favorites"

    def test_deleteAirport(self):
        response_id = requests.get(self.URL, 
                    headers = self.Auth)
        id = response_id.json().get("data")[0].get("id")
        response = requests.delete(f"{self.URL}/{id}", 
                    headers = self.Auth)
        assert_that(response.status_code).is_equal_to(204)