import requests, datetime
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("Vellore Institute of Technology")
latitude = location.latitude
longitude = location.longitude

color = 'yellow'

r = requests.post("http://127.0.0.1:5000/", data={'latitude': latitude, 'longitude': longitude, 'time': datetime.datetime.now(), 'type': color})

print(r.text)