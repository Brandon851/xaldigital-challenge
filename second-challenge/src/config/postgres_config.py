import os
import asyncpg
from typing import Any
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de la base de datos desde las variables de entorno
POSTGRES_USER = os.getenv('POSTGRES_USER', '')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME', '')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '')

async def create_postgres_connection() -> Any:
		"""
		Crear una conexión a la base de datos PostgreSQL.

		Returns:
				Any: Objeto de conexión a la base de datos.
		"""
		# Conectar a la base de datos PostgreSQL
		postgres_connection = await asyncpg.connect(
				user=POSTGRES_USER,
				password=POSTGRES_PASSWORD,
				database=POSTGRES_DB_NAME,
				host=POSTGRES_HOST,
				port=POSTGRES_PORT
		)

		return postgres_connection

async def execute_query(query: str, connection: Any) -> Any:
		"""
		Ejecuta una consulta SQL en la base de datos PostgreSQL.

		Args:
				query (str): La consulta SQL a ejecutar.
				connection (Any): Objeto de conexión a la base de datos.

		Returns:
				Any: El resultado de la consulta.
		"""
		# Ejecutar la consulta SQL
		result = await connection.fetch(query)
		return result