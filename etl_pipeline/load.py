from sqlalchemy import create_engine
from config.settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

def load_data(df, table_name):
    engine = engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    df.to_sql(name = table_name, con=engine, if_exists="replace", index = False)
    print(f"Datos cargados en la tabla {table_name}")