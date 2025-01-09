from sqlalchemy import text
from db import get_db_engine
import pandas as pd

def main():
    engine = get_db_engine()
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1 as TEST"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df)

if __name__ == "__main__":
    main()
