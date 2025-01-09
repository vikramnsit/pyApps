from projects.config import Config
import projects.db
import requests

class Weather:

    def __init__(self):
        super().__init__()
        content = Config.load_config()["weathermap"]
        self.apikey = content['apikey']
        self.part = content['part']
        self.lon = content['longitude']
        self.lat = content['latitude']
        self.api_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={apikey}'

    def extract(self):
        print(self.api_url)
        requests.request()


w = Weather()
w.extract()