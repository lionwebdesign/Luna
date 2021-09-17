import requests

class CURRENT_GEOLOCATION():
    def __init__(self):
        self.data  = {
            "considerIp": "true"
        }
        self.api_key = "AIzaSyA-C2U9OWidR-wfrXZl5OEXbosiVVFOhC0"
        
    def get_location(self):
        url = (f"https://www.googleapis.com/geolocation/v1/geolocate?key={self.api_key}")
        response = requests.post(url, json=self.data)
        location = response.json()["location"]
        lat = location["lat"]
        lng = location["lng"]
        position = [lat, lng]
        return position