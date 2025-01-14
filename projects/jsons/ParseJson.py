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
            # df = pd.DataFrame(file_content, index=[0])
            df = pd.DataFrame(file_content, columns=['Name', 'Age', 'Location'])

            return df

    def parse_nestedjson(self, file_content) -> Optional[str]:
            df = pd.json_normalize(file_content)
            return df

p = ParseJson('ArrayOfArrays.json')
file_content = p.load_file()

df = p.parse_json(file_content)
print(df)