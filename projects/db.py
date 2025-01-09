from sqlalchemy import create_engine
from projects.config import Config

def get_db_engine():
    config = Config.load_config()['database']
    server = config['server']
    database = config['db']
    connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    engine = create_engine(connection_string)
    return engine
