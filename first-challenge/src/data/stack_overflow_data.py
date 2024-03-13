from .item import Item
from .owner import Owner
from typing import Dict, Any, List, Optional

class StackOverflowData:
		def __init__(self, items: List[Item], has_more: bool, quota_max: int, quota_remaining: int) -> None:
				"""
				Constructor de la clase StackOverflowData.

				Args:
						items (List[Item]): Una lista de instancias de la clase Item, cada una representando una pregunta de Stack Overflow.
						has_more (bool): Indica si hay más resultados disponibles.
						quota_max (int): El límite máximo de cuota de la API de Stack Overflow.
						quota_remaining (int): La cantidad de solicitudes restantes que se pueden hacer a la API de Stack Overflow.

				"""
				self.items = items
				self.has_more = has_more
				self.quota_max = quota_max
				self.quota_remaining = quota_remaining

		def __str__(self):
				"""
				Método especial que define la representación en cadena de texto de un objeto StackOverflowData.

				Returns:
						str: La representación en cadena de texto del objeto StackOverflowData.
				"""
				# Utilizamos una f-string para formatear la cadena con todos los atributos del objeto
				return f"StackOverflowData(items={self.items}, has_more={self.has_more}, quota_max={self.quota_max}, " \
								f"quota_remaining={self.quota_remaining})"

		@classmethod
		def from_json(cls, json_data: Dict[str, Any]) -> 'StackOverflowData':
				"""
				Método de clase para crear una instancia de StackOverflowData a partir de un JSON.

				Args:
						json_data (Dict[str, Any]): El JSON que se va a analizar para construir la instancia.

				Returns:
						StackOverflowData: La instancia de StackOverflowData creada a partir del JSON.

				"""
				# Inicializa una lista para almacenar los elementos
				items = []

				# Itera sobre los elementos en el JSON, utilizando una lista vacía si no hay elementos disponibles
				for item_data in json_data.get('items', []):
						# Extrae los datos del propietario del elemento, utilizando un diccionario vacío si no hay datos disponibles
						owner_data = item_data.get('owner', {})
						
						# Crea una instancia de Owner con los datos extraídos
						owner = Owner(
								reputation=owner_data.get('reputation', 0),
								user_id=owner_data.get('user_id', 0),
								user_type=owner_data.get('user_type', ''),
								profile_image=owner_data.get('profile_image', ''),
								display_name=owner_data.get('display_name', ''),
								link=owner_data.get('link', '')
						)
						
						# Crea una instancia de Item con los datos extraídos
						item = Item(
								tags=item_data.get('tags', []),
								owner=owner,
								is_answered=item_data.get('is_answered', False),
								view_count=item_data.get('view_count', 0),
								answer_count=item_data.get('answer_count', 0),
								score=item_data.get('score', 0),
								last_activity_date=item_data.get('last_activity_date', 0),
								creation_date=item_data.get('creation_date', 0),
								last_edit_date=item_data.get('last_edit_date', 0),
								question_id=item_data.get('question_id', 0),
								content_license=item_data.get('content_license', ''),
								link=item_data.get('link', ''),
								title=item_data.get('title', '')
						)
						# Agrega el elemento a la lista de elementos
						items.append(item)

				# Crea y retorna una instancia de StackOverflowData con los elementos y metadatos extraídos
				return cls(
						items=items,
						has_more=json_data.get('has_more', False),
						quota_max=json_data.get('quota_max', 0),
						quota_remaining=json_data.get('quota_remaining', 0)
				)

		def get_answered_count(self) -> int:
				"""
				Obtiene el número de respuestas contestadas.

				Returns:
						int: El número de respuestas contestadas.
				"""
				answered_count: int = sum(1 for item in self.items if item.is_answered)
				return answered_count

		def get_unanswered_count(self) -> int:
				"""
				Obtiene el número de respuestas no contestadas.

				Returns:
						int: El número de respuestas no contestadas.
				"""
				unanswered_count: int = sum(1 for item in self.items if not item.is_answered)
				return unanswered_count

		def get_least_viewed_answer(self) -> Optional[Item]:
				"""
				Obtiene la respuesta con el menor número de vistas.

				Returns:
						Optional[Item]: La respuesta con el menor número de vistas, o None si no hay respuestas disponibles.
				"""
				if not self.items:
						return None
				least_viewed_answer: Item = min(self.items, key=lambda x: x.view_count)
				return least_viewed_answer

		def get_oldest_answer(self) -> Optional[Item]:
				"""
				Obtiene la respuesta más vieja.

				Returns:
						Optional[Item]: La respuesta más vieja.
						Puede contener None si no hay respuestas disponibles.
				"""
				if not self.items:
						return None
				oldest_answer: Item = min(self.items, key=lambda x: x.creation_date)
				return oldest_answer

		def get_latest_answer(self) -> Optional[Item]:
				"""
				Obtiene la respuesta más actual.

				Returns:
						Optional[Item]: La respuesta más actual.
						Puede contener None si no hay respuestas disponibles.
				"""
				if not self.items:
						return None
				latest_answer: Item = max(self.items, key=lambda x: x.creation_date)
				return latest_answer

		def get_answer_of_owner_with_highest_reputation(self) -> Optional[Item]:
				"""
				Obtiene la respuesta del propietario con la mayor reputación.

				Returns:
								Optional[Item]: La respuesta del propietario con la mayor reputación,
																o None si no hay respuestas disponibles.
				"""
				if not self.items:
						return None

				# Encuentra el propietario con la mayor reputación
				owner_with_highest_reputation = max((item.owner for item in self.items), key=lambda x: x.reputation)

				# Encuentra la respuesta del propietario con la mayor reputación
				answer_of_owner_with_highest_reputation = next((item for item in self.items if item.owner == owner_with_highest_reputation), None)

				# Retorna la respuesta del propietario con la mayor reputación
				return answer_of_owner_with_highest_reputation