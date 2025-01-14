import json
import os
from projects import ROOT_DIR
import pandas as pd

with open(os.path.join(ROOT_DIR, 'jsons/AlphaVantage.json'), 'rt') as j:
    json_content = json.load(j)

metadata = json_content['Meta Data']
df_metadata = pd.DataFrame(metadata, index=[0])
df_metadata.rename(columns={"2. Symbol":"Symbol", "3. Last Refreshed":"LastRefreshed", "5. Time Zone":"Timezone"}, inplace=True)
df_metadata_filtered = df_metadata[["Symbol", "LastRefreshed", "Timezone"]]
print(df_metadata_filtered)

content = json_content['Time Series (Daily)']
df = pd.DataFrame.from_dict(content, orient='index')
df.reset_index(inplace=True)

df.rename(columns={"index":"Date", "1. open":"open", "2. high":"high", "3. low":"low", "4. close":"close", "5. volume":"volume"}, inplace=True)


df_metadata_filtered1 = pd.concat([df_metadata_filtered]*len(df), ignore_index=True)
print(df_metadata_filtered1)
final_df = pd.concat([df_metadata_filtered1, df], axis = 1)

print(final_df)

# print(df)
# first_normalized_json = pd.json_normalize(content, record_path='Time Series (Daily)')

# print(first_normalized_json)
#
# content = json_content['Time Series (Daily)']
# df = pd.DataFrame.from_dict(content, orient='index')
# df.reset_index(inplace=True)
# df.rename(columns={'index':'Date'}, inplace=True)
#
# df_metadata = pd.json_normalize(json_content['Meta Data'])
# df_metadata = df_metadata[['2. Symbol', '3. Last Refreshed']]
# df_metadata.rename(columns={
#         '2. Symbol': 'Symbol',
#         '3. Last Refreshed': 'LastRefreshed',
# }, inplace = True)
# df_metadata=pd.concat([df_metadata] * len(df),ignore_index=True)
# df=pd.concat([df_metadata,df],axis =1)

# print(df)

