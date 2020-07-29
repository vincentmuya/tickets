import geocoder
from geopy.geocoders import Nominatim

g = geocoder.ip('me')
g.latlng
g.address
print (g.address)
print (g.latlng)
geolocator = Nominatim(user_agent="user",timeout=10)
location = geolocator.geocode("Nairobi, Kenya")
print(location.latitude, location.longitude)
print(location)

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyC14hiJhxMKNF4T4JCkDWyITjz8CoU2aco')

geocode_result = gmaps.geocode(g)

print(geocode_result)