class Owner:
		def __init__(self, reputation: int, user_id: int, user_type: str, profile_image: str, display_name: str, link: str) -> None:
				"""
				Constructor de la clase Owner.

				Args:
						reputation (int): La reputación del propietario.
						user_id (int): El ID del usuario.
						user_type (str): El tipo de usuario.
						profile_image (str): La URL de la imagen de perfil.
						display_name (str): El nombre de visualización del usuario.
						link (str): El enlace al perfil del usuario.
				"""
				self.reputation = reputation
				self.user_id = user_id
				self.user_type = user_type
				self.profile_image = profile_image
				self.display_name = display_name
				self.link = link

		def __str__(self):
				"""
				Método especial que define la representación en cadena de texto de un objeto Owner.

				Returns:
						str: La representación en cadena de texto del objeto Owner.
				"""
				# Utilizamos una f-string para formatear la cadena con todos los atributos del objeto
				return f"Owner(reputation={self.reputation}, user_id={self.user_id}, user_type={self.user_type}, " \
								f"profile_image={self.profile_image}, display_name={self.display_name}, link={self.link})"
