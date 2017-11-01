import connexion
import psycopg2

from swagger_server.models.cancion import Cancion
from swagger_server.models.canciones import Canciones
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

def conectar():

    conexion = psycopg2.connect(
        database = "MyDB",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )

    return conexion

def lanzarError(msg, status, title, typee):
    d = {}
    d["detail"] = msg
    d["error"] = status
    d["title"] = title
    d["type"] = typee
    return d


def cancion_codigo_get(codigo):
    """
    Devuelve una cancion
    Devuelve una única cancion por su código
    :param codigo: Numero de codigo de la cancion
    :type codigo: int

    :rtype: Cancion
    """

    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT row_to_json(cancion) \
         FROM cancion \
         WHERE codigo = " + str(codigo) + ";"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("Cancion no encontrada", 404, "WTF", "about:blank")

    else:
        return rows[0][0]


def cancion_codigo_post(cancion):
    """
    Crea una cancion
    Añade una nueva cancion a la lista
    :param cancion: La cancion creada
    :type cancion: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        cancion = Cancion.from_dict(connexion.request.get_json())

    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "INSERT INTO cancion VALUES ("
        + str(cancion.codigo) + ","
        + "'" + cancion.titulo + "',"
        + "'" + cancion.artista + "',"
        + str(cancion.duracion) + ");"
    )

    conex.commit()
    conex.close()

    return "Inserción de cancion {} realizada con exito".format(cancion.codigo)


def obtener_canciones(nCanciones=None):
    """
    Obtiene algunas canciones
    Devuelve una lista con varias canciones
    :param nCanciones: Numero de canciones devueltas
    :type nCanciones: int

    :rtype: Canciones
    """

    conex = conectar()
    cursor = conex.cursor()

    cursor.execute(
        "SELECT array_to_json(array_agg(row_to_json(t))) \
         FROM ( \
                SELECT * \
                FROM cancion \
                WHERE codigo BETWEEN 1 AND "+ str(nCanciones) 
                + ") t"
    )

    rows = cursor.fetchall()

    conex.close()

    if len(rows) == 0:
        return lanzarError("No hay canciones", 404, "WTF", "about:blank")

    else:
        return rows[0][0]