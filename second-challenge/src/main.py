import asyncio
from config.postgres_config import create_postgres_connection, execute_query

async def main():
		# Crear la conexión a la base de datos
		connection = await create_postgres_connection()

		# Consultas SQL
		queries = [
				# 1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?
				"""
						SELECT aeropuertos.NOMBRE_AEROPUERTO, COUNT(vuelos.ID_MOVIMIENTO) AS total_movimientos
						FROM vuelos
						INNER JOIN aeropuertos ON vuelos.ID_AEROPUERTO = aeropuertos.ID_AEROPUERTO
						GROUP BY aeropuertos.NOMBRE_AEROPUERTO
						ORDER BY total_movimientos DESC
						LIMIT 1;
				""",
				# 2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?
				"""
						SELECT aerolineas.NOMBRE_AEROLINEA, COUNT(vuelos.ID_AEROLINEA) AS total_vuelos
						FROM vuelos
						INNER JOIN aerolineas ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
						GROUP BY aerolineas.NOMBRE_AEROLINEA
						ORDER BY total_vuelos DESC
						LIMIT 1;
				""",
				# 3. ¿En qué día se han tenido mayor número de vuelos?
				"""
						SELECT DIA, COUNT(*) AS total_vuelos
						FROM vuelos
						GROUP BY DIA
						ORDER BY total_vuelos DESC
						LIMIT 1;
				""",
				# 4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?
				"""
						SELECT aerolineas.NOMBRE_AEROLINEA, vuelos.DIA, COUNT(*) AS total_vuelos
						FROM vuelos
						INNER JOIN aerolineas ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
						GROUP BY aerolineas.NOMBRE_AEROLINEA, vuelos.DIA
						HAVING COUNT(*) > 2;
				"""
		]

		# Ejecutar las consultas
		for i, query in enumerate(queries, start=1):
				result = await execute_query(query, connection)
				print(f"Resultado de la consulta {i}: {result}")

		# Cerrar la conexión
		await connection.close()

if __name__ == "__main__":
		asyncio.run(main())