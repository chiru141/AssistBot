import requests
from pprint import pprint


ZOMATO_API_KEY ="bdb3b7c195a74c2b0deefe4534c6a410"

#categoryUrl = "https://developers.zomato.com/api/v2.1/categories" 

locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/cities?lat=28&lon=77"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ZOMATO_API_KEY"}

response = requests.get(locationUrlFromLatLong, headers=header)

pprint(response.json())
