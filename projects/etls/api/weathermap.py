
from sqlalchemy import text, create_engine
import pyodbc
from projects.config import Config
import pandas as pd
import sqlalchemy as sa

content = Config.load_config(Config)

SERVER = content["database"]["server"]
DATABASE = content["database"]["db"]

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
# connectionString1 = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
#
conn = pyodbc.connect(connectionString)
print("Connection successful!")
cursor = conn.cursor()
SQL = "SELECT * FROM dbo.weather"

cursor.execute(SQL)
rows = cursor.fetchall()

# print(df)
#
# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT 1"))
#         print(f"Connected successfully to {SERVER}");
# except Exception as e:
#     print("Connection failed:", e)
