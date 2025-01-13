import json
import os
from projects import ROOT_DIR
import pandas as pd

with open(os.path.join(ROOT_DIR,'AlphaVantage.json'), 'rt') as j:
    json_content = json.load(j)

print(json_content)

content = json_content['Time Series (Daily)']
df = pd.DataFrame.from_dict(content, orient='index')
df.reset_index(inplace=True)
df.rename(columns={'index':'Date'}, inplace=True)
print(df)
