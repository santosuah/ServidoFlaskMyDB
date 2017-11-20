## API Canción
API Rest de canciones usando la base de datos MyDB de la PECL1, implementación del la conexion entre la base y el servidor flask, y las operaciones (GET, POST).

#### Dependecias
- PostgreSQL
- Python 3.x
- Psycopg2
- Flask

#### Instalar:
1. Crear una base de datos en Postgres con nombre **MyDB** y esquema el del archivo `tabla_cancion.sql`
2. Instalar *Pyhton* y en la terminal instalar *Flask*  `$ pip install flask`
3. Instalar el conector de *PostgreSQL* con python *Psycopg2*  `$ pip install psycopg2`
4. Ejecutar el servidor *Flask*  `$ py run.py`

Configuracion de la **conexión**:

```python
def conectar():
    conexion = psycopg2.connect(
        database = "MyDB",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )
    return conexion
```