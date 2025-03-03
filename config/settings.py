import os
from dotenv import load_dotenv

# Cargamos las variables del archivo .env
load_dotenv()

# Credenciales
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = '127.0.0.1'
DB_NAME = 'movies'

# Validación
if not DB_USER or not DB_PASSWORD:
    raise ValueError("Las crenciales no estan definidas")