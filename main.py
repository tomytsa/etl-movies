import os
import pandas as pd
import mysql.connector
import pymysql
from sqlalchemy import create_engine
# Conectar base de datos MySQL
db_user = os.getenv("DB-USER")
db_password = os.getenv("DB-PASSWORD")
if not db_user or not db_password:
    raise ValueError("Las credenciales no estan definidas en las variables de entorno")
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = db_user,
    password = db_password,
    database = "movies"
)
cursor = mydb.cursor()
mydb.commit()

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@127.0.0.1/movies")


myvar.to_sql(name = "movies", con = engine, if_exists = "append", index = False)