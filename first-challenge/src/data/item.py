from typing import List
from .owner import Owner

class Item:
		def __init__(self, tags: List[str], owner: Owner, is_answered: bool, view_count: int, answer_count: int,
									score: int, last_activity_date: int, creation_date: int, last_edit_date: int, question_id: int,
									content_license: str, link: str, title: str) -> None:
				"""
				Constructor de la clase Item.

				Args:
						tags (List[str]): Una lista de etiquetas asociadas con la pregunta.
						owner (Owner): El propietario de la pregunta (instancia de la clase Owner).
						is_answered (bool): Indica si la pregunta ha sido respondida.
						view_count (int): El número de vistas que ha recibido la pregunta.
						answer_count (int): El número de respuestas que ha recibido la pregunta.
						score (int): La puntuación de la pregunta.
						last_activity_date (int): La fecha de la última actividad en la pregunta (en formato de fecha Unix).
						creation_date (int): La fecha de creación de la pregunta (en formato de fecha Unix).
						last_edit_date (int): La fecha de la última edición de la pregunta (en formato de fecha Unix).
						question_id (int): El ID único de la pregunta.
						content_license (str): La licencia de contenido asociada con la pregunta.
						link (str): El enlace a la pregunta en Stack Overflow.
						title (str): El título de la pregunta.
				"""
				self.tags = tags
				self.owner = owner
				self.is_answered = is_answered
				self.view_count = view_count
				self.answer_count = answer_count
				self.score = score
				self.last_activity_date = last_activity_date
				self.creation_date = creation_date
				self.last_edit_date = last_edit_date
				self.question_id = question_id
				self.content_license = content_license
				self.link = link
				self.title = title

		def __str__(self):
				"""
				Método especial que define la representación en cadena de texto de un objeto Item.

				Returns:
						str: La representación en cadena de texto del objeto Item.
				"""
				# Utilizamos una f-string para formatear la cadena con todos los atributos del objeto
				return f"Item(tags={self.tags}, owner={self.owner}, is_answered={self.is_answered}, view_count={self.view_count}, " \
								f"answer_count={self.answer_count}, score={self.score}, last_activity_date={self.last_activity_date}, " \
								f"creation_date={self.creation_date}, last_edit_date={self.last_edit_date}, question_id={self.question_id}, " \
								f"content_license={self.content_license}, link={self.link}, title={self.title})"
