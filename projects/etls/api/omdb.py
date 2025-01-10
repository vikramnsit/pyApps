import pandas as pd
import json
from projects.config import Config
import projects.db as db
from projects.services.ApiClient import ApiClient


class Movies:

    def __init__(self):
        super().__init__()
        content = Config.load_config()["omdb"]
        self.apikey = content['apikey']
        self.api_url = f'http://www.omdbapi.com/?i=tt0111161&apikey={self.apikey}&'

    def extract(self):
        print(self.api_url)
        headers = {
            "Api-Key": {self.apikey},
            "Accept": "application/json"
        }

        apiclient = ApiClient()
        response = apiclient.get(self.api_url)

        if response.status_code == 200:
            api_content = response.json()
            df = pd.DataFrame(api_content)
            df['Ratings'] = df['Ratings'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)
            print(df)
            return df
        else:
            status = response.status_code
            print(f'Bad request: {status}')

    def load(self, df:pd.DataFrame):
        engine = db.get_db_engine()
        df.to_sql("Movies", engine, index=False, if_exists="append")
        print('Data is successfully loaded in the table')

w = Movies()
df = w.extract()
w.load(df)