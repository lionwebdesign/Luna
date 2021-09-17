import requests, json

class CLIMA():
    def __init__(self):
        self.api_key = "f1e4695138a9aa78063b3515d1b84957"
    
    def get_clima(self, city_name):
        self.city = city_name
        self.requests_base_url = (f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&lang=sp&units=metric&appid={self.api_key}")
        self.response = requests.get(self.requests_base_url)
        self.x = self.response.json()
        if self.x["cod"] != "404":
            self.y = self.x["main"]
            self.current_temperature = self.y["temp"]
            self.current_pressure = self.y["pressure"]
            self.current_humidity = self.y["humidity"]
            self.z = self.x["weather"]
            self.weather_description = self.z[0]["description"]
            resultado = (f"La temperatura es de {str(self.current_temperature)}°C, presión Atmosferica de {str(self.current_pressure)} hPa, {str(self.current_humidity)}% de humedad, con {str(self.weather_description)}")
            return resultado
        else:
            resultado = (f"Lo siento no encontre {self.city} en mi base de datos")   
            return resultado
