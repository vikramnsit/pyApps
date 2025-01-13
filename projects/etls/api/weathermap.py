import pandas as pd
import logging
from projects import db
from projects.config import Config
from projects.services.ApiClient import ApiClient

log = logging.getLogger(__name__)

class Weather:

    def __init__(self):
        super().__init__()
        content = Config.load_config()["weathermap"]
        self.apikey = content['apikey']
        self.part = content['part']
        self.lon = content['longitude']
        self.lat = content['latitude']
        self.api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.apikey}'

    def extract(self):
        print(f'Vendor API URL: {self.api_url}')

        headers = {
            "Api-Key": {self.apikey},
            "Accept": "application/json"
        }

        # response = requests.get(self.api_url)
        apiclient = ApiClient()
        response = apiclient.get(self.api_url)

        if response.status_code == 200:
            print(f'API Status Code: {response.status_code}')
            api_content = response.json()
            main_json = pd.json_normalize(api_content)
            weather_json = pd.json_normalize(main_json['weather'])
            final_json = pd.concat([main_json, weather_json], axis=1)

            selected_columns = ['weather', 'base', 'visibility', 'dt', 'timezone', 'id', 'name', 'cod', 'main.temp',
                                'main.feels_like', 'main.temp_min', 'main.temp_max', 'main.pressure', 'main.humidity']
            final_json = final_json[selected_columns]
            # print(final_json['weather'])
            df = pd.DataFrame(final_json)
            log.info(f'Dataframe successfully created')
            return df
        else:
            status = response.status_code
            print(f'Bad request: {status}')

    def load(self, df: pd.DataFrame):
        engine = db.get_db_engine()
        df.to_sql("WeatherMap", engine, index=False, if_exists="append")
        log.info(f'Data is successfully loaded in the table')


w = Weather()
df = w.extract()
w.load(df)
