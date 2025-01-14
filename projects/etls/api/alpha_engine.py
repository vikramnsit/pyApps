from projects import db
from projects.services.ApiClient import ApiClient
from projects.config import Config
import pandas as pd

class AlphaEngine(ApiClient):

    def __init__(self):
        super().__init__()
        self.apiKey = Config.load_config()['alpha_advantage']
        self.apiURL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey={self.apiKey}'

    def extract(self):
        api = ApiClient()
        try:
            apiResponse = api.get(url=self.apiURL)

            if apiResponse.status_code == 200:
                try:
                    content = apiResponse.json()
                    print(f'{apiResponse.content}')
                    timeseries = content['Time Series (Daily)']
                    print(f'{content}')
                    time_series_df = pd.DataFrame.from_dict(timeseries, orient='index')
                    time_series_df.reset_index(inplace=True)
                    time_series_df.rename(columns={'index': 'Date'}, inplace=True)
                    meta_data = pd.json_normalize(content['Meta Data'])
                    meta_data = meta_data[['2. Symbol', '3. Last Refreshed', '4. Time Zone']]  # Select only relevant columns

                    # Add meta data to the time series DataFrame
                    meta_data = pd.concat([meta_data] * len(time_series_df), ignore_index=True)
                    final_df = pd.concat([meta_data, time_series_df], axis=1)

                    # Optional: Rename columns for clarity
                    final_df.rename(columns={
                        '2. Symbol': 'Symbol',
                        '3. Last Refreshed': 'LastRefreshed',
                        '4. Time Zone': 'TimeZone'
                    }, inplace=True)
                except Exception as e:
                    print(f'Error in parsing json data from API: {repr(e)}')
        except Exception as e:
            print(f'Error in getting data from API: {Exception}')

    def transform(self):
        pass

    def load(self):
        pass


a = AlphaEngine()
a.extract()