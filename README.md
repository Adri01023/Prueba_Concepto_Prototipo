# Prueba de concepto: API de análisis de datos

## Descripción

Esta prueba de concepto está pensada para demostrar la interconectividad entre todas las dependencias involucradas en el proyecto.

El backend se basa en una API REST que:

* consulta datos desde una base de datos SQLite
* procesa los datos utilizando Pandas
* genera una visualización mediante Matplotlib

El frontend realiza peticiones a la API y muestra los datos y la gráfica generada.

---

# Dependencias utilizadas

* Python 3.12
* FastAPI
* Pandas
* SQLAlchemy
* Uvicorn (no incluida en el Anteproyecto pero necesaria ya que actua como servidor web)
* SQLite
* Matplotlib
* HTML + JavaScript (front simple para demostración de la prueba de concepto)

El proyecto se ha desarrollado utilizando PyCharm y todos los comandos se han ejecutado desde la consola integrada del IDE.

---

# Descripción de los archivos:

* main.py → servidor API con FastAPI
* bd.py → script que crea la base de datos e inserta datos de prueba
* requerimientos.txt → dependencias del proyecto
* frontend/index.html → interfaz web que consume la API

---

# Configuración del proyecto

## 1. Crear el proyecto en PyCharm

1. Abrir PyCharm
2. Seleccionar New Project
3. Elegir Project venv
4. En Python version elegir Python 3.12
5. Crear el proyecto

El entorno virtual se crea automáticamente.

---

# Instalación de dependencias

Todas las dependencias se instalan desde la consola interna de PyCharm.

Ejecutar:

pip install -r requerimientos.txt

---

# Crear la base de datos

Ejecutar el archivo bd.py

---

# Ejecutar el servidor API

Para iniciar el backend ejecutar en la consola interna de PyCharm:

uvicorn main:app --reload

El servidor se iniciará en:

http://127.0.0.1:8000

---

# Documentación automática de la API

FastAPI genera automáticamente una documentación interactiva accesible en:

http://127.0.0.1:8000/docs

Desde esta interfaz es posible probar todos los endpoints.

---

# Endpoints disponibles

### Obtener datos

GET /data

Devuelve los datos almacenados en la base de datos en formato JSON.

---

### Obtener gráfica

GET /plot

Genera una gráfica con Matplotlib a partir de los datos almacenados.

---

# Ejecutar el frontend

Abrir el archivo:

frontend/index.html

El frontend permite:

1. realizar una petición a la API
2. mostrar los datos obtenidos
3. visualizar la gráfica generada por el backend

---

# Conclusión

Con esta prueba de concepto se establecen las dependencias y sus respectivas versiones que se van a usar (previsiblemente) en el proyecto, gracias a esta prueba de concepto
se ha descubierto la necesidad de una nueva dependencia (Uvicorn) que actua como servidor web, las versiones de las dependencias se encuentran en el fichero requerimientos.txt que se encuentra en este mismo repositorio.
