import requests
import pytest

def test_getAllResponse():

    responseFetch = requests.get("https://airportgap.dev-tester.com/api/airports/")
    assert responseFetch.status_code == 200
    # pprint(responseFetch.json())
    assert len(responseFetch.json().get("data")) == 30

def test_getOneResponse():
    airport_id = "GKA"
    responseFetch2 = requests.get(f"https://airportgap.dev-tester.com/api/airports/{airport_id}")
    assert responseFetch2.status_code == 200
    data = responseFetch2.json().get("data")
    assert data["id"] == "GKA"
    assert data["attributes"]["city"] == "Goroka"
    assert data["attributes"]["icao"] == "AYGA"
    assert data["attributes"]["altitude"] == 5282

def test_getNotFound():
    airport_id = "CGKA"
    responseFetch3 = requests.get(f"https://airportgap.dev-tester.com/api/airports/{airport_id}")
    assert responseFetch3.status_code == 404 
   # assert "The page you requested could not be found" not in responseFetch3.text
    assert "The page you requested could not be found" in responseFetch3.text
    