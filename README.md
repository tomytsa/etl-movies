# ETL con Python, Pandas y MySQL

## Descripción
Este proyecto implementa un pipeline de ETL (Extracción, Transformación y Carga) utilizando Python, Pandas y MySQL.
Se extraen datos desde un archivo CSV, se procesan y limpian, y finalmente se cargan en una base de datos MySQL.

## Tecnologías utilizadas
- Python 3
- Pandas
- MySQL
- SQLAlchemy
- dotenv (para gestión de variables de entorno)

## Estructura del Proyecto
```
ETL-Project/
│── data/
│   ├── top1000.csv  # Archivo de datos fuente
│── etl/
│   ├── extract.py   # Módulo de extracción de datos
│   ├── transform.py # Módulo de transformación de datos
│   ├── load.py      # Módulo de carga de datos
│── .env             # Archivo con credenciales (no subir a GitHub)
│── main.py          # Script principal para ejecutar el ETL
│── README.md        # Documentación del proyecto
│── requirements.txt # Lista de dependencias
```

## Instalación y configuración
1. Clona este repositorio:
   ```sh
   git clone https://github.com/tuusuario/etl-movies.git
   cd etl-movies
   ```
2. Crea un entorno virtual y actívalo:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows
   ```
3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Configura las credenciales en un archivo `.env` en la raíz del proyecto:
   ```env
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_HOST=127.0.0.1
   DB_NAME=movies
   ```

## Uso
1. Asegúrate de que MySQL está en ejecución y la base de datos `movies` está creada.
2. Ejecuta el pipeline ETL:
   ```sh
   python main.py
   ```

## Explicación del código
El proceso ETL se divide en tres módulos:
1. **Extracción (`extract.py`)**: Carga los datos desde un archivo CSV en un DataFrame de Pandas.
2. **Transformación (`transform.py`)**: Aplica limpieza y eliminación de columnas innecesarias.
3. **Carga (`load.py`)**: Inserta los datos procesados en una tabla de MySQL utilizando SQLAlchemy.

## Mejoras futuras
- Agregar validación y control de calidad de los datos.
- Implementar Airflow para la orquestación del pipeline.
- Mejorar la escalabilidad con una base de datos en la nube.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

