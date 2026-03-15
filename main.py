# main.py

# Framework de API
from fastapi import FastAPI

# Para devolver imágenes
from fastapi.responses import StreamingResponse

# Para permitir peticiones desde el front (html)
from fastapi.middleware.cors import CORSMiddleware

# Base de datos
from sqlalchemy import create_engine, text

# Análisis de datos
import pandas as pd

# Gráficas
import matplotlib.pyplot as plt

# Manejo de memoria
import io


# Creamos aplicación FastAPI
app = FastAPI()

# Permitir peticiones desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permitir todos (para prueba de concepto)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión con base de datos SQLite
engine = create_engine("sqlite:///datos.db")


# ENDPOINT 1
# Devuelve datos de la base de datos en JSON
@app.get("/data")
def get_data():

    # Consulta SQL
    query = text("SELECT * FROM ventas")

    # Ejecutamos consulta pasada a DataFrame (pandas)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    # Convertimos dataframe a JSON
    return df.to_dict(orient="records")



# ENDPOINT 2
# Genera gráfica con matplotlib
@app.get("/plot")
def get_plot():

    query = text("SELECT * FROM ventas")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    # Crear gráfica
    fig, ax = plt.subplots()
    ax.plot(df["mes"], df["ventas"])

    # Guardar imagen en memoria
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    # Devolver imagen al navegador
    return StreamingResponse(img, media_type="image/png")