from pprint import pprint
import requests

responseFetch = requests.get("https://airportgap.dev-tester.com/api/airports/")
print(responseFetch.status_code)
# print(responseFetch.json())

#pprint(responseFetch.json())
pprint(len(responseFetch.json().get("data")))

assert len(responseFetch.json().get("data")) > 1

# pprint is used for wrap the json result

responseFetch2 = requests.get("https://airportgap.dev-tester.com/api/airports/GKA")
print(responseFetch2.status_code)
# print(responseFetch.json())

#pprint(responseFetch2.json().get("data"))