
import requests
import json

apiBase = "http://localhost:8080/miAplicacion/"


# get de cancion por codigo

codigo = 200

r1 = requests.get(apiBase + "cancion/" + str(codigo))
cancion = r1.json()

print(cancion)
print()

# get de lista de canciones
# http://localhost:8080/miAplicacion/canciones?nCanciones=3

nCanciones = 3

r2 = requests.get(apiBase + "canciones?nCanciones=" + str(nCanciones))
canciones = r2.json()

for c in canciones:
	print(c)

# post de cancion
# http://localhost:8080/miAplicacion/cancion
# no va todavia
# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

carga = {
	"artista": "string",
	"codigo": 0,
	"duracion": 0,
	"titulo": "string"
}

r3 = requests.post(apiBase + "cancion", data = json.dumps(carga))
print(r3.text)