# init_db.py

# Importamos herramientas de SQLAlchemy
from sqlalchemy import create_engine, text

# Creamos conexión a SQLite
# Si el archivo no existe se crea automáticamente
engine = create_engine("sqlite:///datos.db")

# Abrimos conexión
with engine.connect() as conn:

    # Creamos tabla de ejemplo
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS ventas (
        mes TEXT,
        ventas INTEGER
    )
    """))

    # Borramos datos anteriores (para evitar duplicados)
    conn.execute(text("DELETE FROM ventas"))

    # Insertamos datos de prueba
    conn.execute(text("""
    INSERT INTO ventas VALUES
    ('Enero',120),
    ('Febrero',150),
    ('Marzo',90),
    ('Abril',200)
    """))

    # Guardamos cambios
    conn.commit()

print("Base de datos creada correctamente")