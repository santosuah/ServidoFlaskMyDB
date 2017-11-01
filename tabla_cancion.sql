CREATE TABLE "cancion"
(
	codigo numeric NOT NULL,
	titulo text,
	artista text,
	duracion real,
	CONSTRAINT cancion_pkey PRIMARY KEY (codigo)
);