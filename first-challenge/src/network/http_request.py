import json
import chardet
import requests
from typing import Any

class HTTPRequest:
		def __init__(self) -> None:
				"""
				Constructor de la clase HTTPRequest.

				Este constructor no toma ningún parámetro
				"""
				pass

		def make_request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
				"""
				Realiza una solicitud HTTP con el método especificado a la URL dada.

				Args:
						method (str): El método de la solicitud HTTP (GET, POST, PUT, DELETE).
						url (str): La URL a la que se enviará la solicitud.
						**kwargs: Argumentos adicionales que se pasarán a la función de solicitud de requests.

				Returns:
						requests.Response: El objeto de respuesta de la solicitud.
				"""
				# Validamos que el método sea válido
				if method.upper() not in ['GET', 'POST', 'PUT', 'DELETE']:
						raise ValueError("Método de solicitud no válido. Debe ser GET, POST, PUT o DELETE.")

				# Realizamos la solicitud HTTP
				response: requests.Response = requests.request(method.upper(), url, **kwargs)

				# Verificamos si la solicitud fue exitosa (código de estado 200)
				if response.status_code == 200:
						# Devolvemos el contenido de la respuesta en formato JSON
						json_bytes: bytes = response.content
						encoding_result: chardet.ResultDict = chardet.detect(json_bytes)
						encoding: str = encoding_result.get('encoding', 'utf-8')
						json_string = json_bytes.decode(encoding)
						json_object = json.loads(json_string)
						return json_object
				else:
						# Si la solicitud no fue exitosa, lanzamos una excepción con el código de estado
						raise Exception(f"Solicitud HTTP fallida. Código de estado: {response.status_code}")