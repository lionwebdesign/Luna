import requests
from general.variables import GENERAL_VARIABLES

class CURRENT_GEOLOCATION():
    def __init__(self):
        self.variables = GENERAL_VARIABLES()
        self.api_key = self.variables.geo_api
        self.data  = {
            "considerIp": "true"
        }
        
    def get_location(self):
        url = (f"https://www.googleapis.com/geolocation/v1/geolocate?key={self.api_key}")
        response = requests.post(url, json=self.data)
        location = response.json()["location"]
        lat = location["lat"]
        lng = location["lng"]
        position = [lat, lng]
        return position