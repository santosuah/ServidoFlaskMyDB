# API Canción
API Rest de canciones usando la base de datos MyDB de la PECL1, implementación del la conexion entre la base y el servidor flask, y las operaciones (GET, POST).

##### Dependecias:
- PostgreSQL
- Python 3.x
- Psycopg2
- Flask

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