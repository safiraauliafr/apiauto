from pprint import pprint
import requests
from assertpy import assert_that

responseFetch = requests.get("https://airportgap.dev-tester.com/api/airports/")
print(responseFetch.status_code)
# print(responseFetch.json())

status = responseFetch.status_code
print(type(status))

if status == 200:
    # print('True')
    pprint(responseFetch.text)
    pprint(len(responseFetch.json().get("data")))
    assert len(responseFetch.json().get("data")) > 1

else:
    print('False')     

# if status code is equal to 200, then print the data

# pprint is used for wrap the json result

responseFetch2 = requests.get("https://airportgap.dev-tester.com/api/airports/GKA")
print(responseFetch2.status_code)
# print(responseFetch.json())

#pprint(responseFetch2.json().get("data"))