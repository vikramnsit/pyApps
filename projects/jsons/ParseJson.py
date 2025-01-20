import json
from typing import Optional
import pandas as pd

class ParseJson:
    def __init__(self, filename):
        self.filename = filename

    def load_file(self) -> Optional[str]:
        try:
            with open(self.filename, 'rt') as r:
                file_content = json.loads(r.read())
                return file_content

        except FileNotFoundError as f:
            print(f'{self.filename} not found!!')
            return None

    def parse_json(self, file_content) -> Optional[str]:
            # Create a DataFrame directly from the 'items' list
            df = pd.DataFrame(file_content['items'])

            # Pivot the DataFrame to restructure it
            reshaped_df = df.set_index('key')



            # Reset the index to flatten the DataFrame
            reshaped_df = reshaped_df.reset_index(drop=True)
            # df = pd.DataFrame(content, index=[0])
            # df = pd.DataFrame(file_content, columns=['Name', 'Age', 'Location'])

            return reshaped_df

    def parse_nestedjson(self, file_content) -> Optional[str]:
            df = pd.DataFrame(file_content['Time Series (Daily)']).T
            df = df.rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"})
            df.reset_index(inplace=True)
            df.rename(columns={"index":"date"}, inplace=True)
            df_main = pd.json_normalize(file_content['Meta Data'])
            df_main = df_main[['2. Symbol', '3. Last Refreshed']]
            df_main.rename(columns={"2. Symbol": "Symbol", "3. Last Refreshed": "LastRefreshed"}, inplace=True)
            metadata = pd.concat([df_main] * len(df), ignore_index=True)
            df = pd.concat([metadata, df], axis = 1)
            
            # df_normalize = pd.json_normalize(file_content, record_path=['departments'])
            return df

p = ParseJson('AlphaVantage.json')
file_content = p.load_file()

df = p.parse_nestedjson(file_content)
print(df)