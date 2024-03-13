-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS vuelos_mexico;

-- Seleccionar la base de datos
USE vuelos_mexico;

-- Crear tabla de aerolineas
CREATE TABLE IF NOT EXISTS aerolineas (
		ID_AEROLINEA INT PRIMARY KEY,
		NOMBRE_AEROLINEA VARCHAR(100) NOT NULL
);

-- Crear tabla de aeropuertos
CREATE TABLE IF NOT EXISTS aeropuertos (
		ID_AEROPUERTO INT PRIMARY KEY,
		NOMBRE_AEROPUERTO VARCHAR(100) NOT NULL
);

-- Crear tabla de movimientos
CREATE TABLE IF NOT EXISTS movimientos (
		ID_MOVIMIENTO INT PRIMARY KEY,
		DESCRIPCION VARCHAR(100) NOT NULL
);

-- Crear tabla de vuelos
CREATE TABLE IF NOT EXISTS vuelos (
		ID_VUELO INT PRIMARY KEY,
		ID_AEROLINEA INT,
		ID_AEROPUERTO INT,
		ID_MOVIMIENTO INT,
		DIA DATE,
		FOREIGN KEY (ID_AEROLINEA) REFERENCES aerolineas(ID_AEROLINEA),
		FOREIGN KEY (ID_AEROPUERTO) REFERENCES aeropuertos(ID_AEROPUERTO),
		FOREIGN KEY (ID_MOVIMIENTO) REFERENCES movimientos(ID_MOVIMIENTO)
);

-- Insertar datos en la tabla aerolineas
INSERT INTO aerolineas (ID_AEROLINEA, NOMBRE_AEROLINEA) VALUES
(1, 'Volaris'),
(2, 'Aeromar'),
(3, 'Interjet'),
(4, 'Aeromexico');

-- Insertar datos en la tabla aeropuertos
INSERT INTO aeropuertos (ID_AEROPUERTO, NOMBRE_AEROPUERTO) VALUES
(1, 'Benito Juarez'),
(2, 'Guanajuato'),
(3, 'La Paz'),
(4, 'Oaxaca');

-- Insertar datos en la tabla movimientos
INSERT INTO movimientos (ID_MOVIMIENTO, DESCRIPCION) VALUES
(1, 'Salida'),
(2, 'Llegada');

-- Insertar datos en la tabla vuelos
INSERT INTO vuelos (ID_VUELO, ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, DIA) VALUES
(1, 1, 1, 1, '2021-05-02'),
(2, 2, 1, 1, '2021-05-02'),
(3, 3, 2, 2, '2021-05-02'),
(4, 4, 3, 2, '2021-05-02'),
(5, 1, 3, 2, '2021-05-02'),
(6, 2, 1, 1, '2021-05-02'),
(7, 2, 3, 1, '2021-05-04'),
(8, 3, 4, 1, '2021-05-04'),
(9, 3, 4, 1, '2021-05-04');

-- QUERIES

-- 1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?

-- Selecciona el nombre del aeropuerto y cuenta el total de movimientos (salidas o llegadas) para cada uno
SELECT aeropuertos.NOMBRE_AEROPUERTO, COUNT(vuelos.ID_MOVIMIENTO) AS total_movimientos
FROM vuelos
-- Une la tabla de vuelos con la tabla de aeropuertos usando el ID del aeropuerto
INNER JOIN aeropuertos ON vuelos.ID_AEROPUERTO = aeropuertos.ID_AEROPUERTO
-- Agrupa los resultados por nombre de aeropuerto
GROUP BY aeropuertos.NOMBRE_AEROPUERTO
-- Ordena los resultados en orden descendente según el total de movimientos
ORDER BY total_movimientos DESC
-- Selecciona solo el primer resultado (el aeropuerto con el mayor número de movimientos)
LIMIT 1;

-- 2. ¿Cuál es el nombre de la aerolínea que ha realizado el mayor número de vuelos durante el año?

-- Selecciona el nombre de la aerolínea y cuenta el total de vuelos para cada una
SELECT aerolineas.NOMBRE_AEROLINEA, COUNT(vuelos.ID_AEROLINEA) AS total_vuelos
FROM vuelos
-- Une la tabla de vuelos con la tabla de aerolíneas usando el ID de la aerolínea
INNER JOIN aerolineas ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
-- Agrupa los resultados por nombre de aerolínea
GROUP BY aerolineas.NOMBRE_AEROLINEA
-- Ordena los resultados en orden descendente según el total de vuelos
ORDER BY total_vuelos DESC
-- Selecciona solo el primer resultado (la aerolínea con el mayor número de vuelos)
LIMIT 1;

-- 3. ¿En qué día se han tenido mayor número de vuelos?

-- Selecciona el día y cuenta el total de vuelos para cada uno
SELECT DIA, COUNT(*) AS total_vuelos
FROM vuelos
-- Agrupa los resultados por día
GROUP BY DIA
-- Ordena los resultados en orden descendente según el total de vuelos
ORDER BY total_vuelos DESC
-- Selecciona solo el primer resultado (el día con el mayor número de vuelos)
LIMIT 1;

-- 4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?

-- Selecciona el nombre de la aerolínea y la fecha, y cuenta el total de vuelos para cada combinación de aerolínea y fecha
SELECT aerolineas.NOMBRE_AEROLINEA, vuelos.DIA, COUNT(*) AS total_vuelos
FROM vuelos
-- Une la tabla de vuelos con la tabla de aerolíneas usando el ID de la aerolínea
INNER JOIN aerolineas ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
-- Agrupa los resultados por nombre de aerolínea y fecha
GROUP BY aerolineas.NOMBRE_AEROLINEA, vuelos.DIA
-- Filtra los resultados para incluir solo las combinaciones de aerolínea y fecha con más de 2 vuelos
HAVING COUNT(*) > 2;
