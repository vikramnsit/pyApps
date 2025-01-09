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
        self.api_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&exclude={self.part}&appid={self.apikey}'

    def extract(self):
        print(self.api_url)
        headers = {
            "Api-Key": {self.apikey},
            "Accept": "application/json"
        }

        response = requests.get(self.api_url, headers=headers)

        if response.status_code == 200:
            api_content = response.json()
            print(api_content)
        else:
            status = response.status_code
            print(f'Bad request: {status}')


w = Weather()
w.extract()
