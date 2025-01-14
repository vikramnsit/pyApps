import pandas as pd
import json
import projects.db as db
import projects.services.ApiClient as api

from projects.config import Config
from requests import exceptions as e


class Movies:

    def __init__(self):
        super().__init__()
        content = Config.load_config()["omdb"]
        self.apikey = content['apikey']
        self.api_url = f'http://www.omdbapi.com/?i=tt0111161&apikey={self.apikey}&'

    def extract(self):

        headers = {
            "Api-Key": self.apikey,
            "Accept": "application/json"
        }

        apiclient = api.ApiClient()
        try:
            response = apiclient.get(self.api_url, headers=headers)

            if response is None:
                raise e.HTTPError('No response from API!!!! Check API url and headers')

        except e.HTTPError as http_err:
            print(f'HTTP Error occurred: {http_err}')
            raise
        except e.ConnectionError as conn_err:
            print(f'Connection Error occurred: {conn_err}')
        except e.RequestException as req_err:
            print(f'An error occurred: {req_err}')

        if response.status_code == 200:
            api_content = response.json()
            df = pd.DataFrame(api_content)
            df['Ratings'] = df['Ratings'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)

            print('Data successfully fetched from API')
            return df
        else:
            status = response.status_code
            print(f'Bad request: {status}')

    def load(self, df: pd.DataFrame):
        engine = db.get_db_engine()
        df.to_sql("Movies", engine, index=False, if_exists="append")
        print('Data is successfully loaded in the table')


w = Movies()
df = w.extract()
