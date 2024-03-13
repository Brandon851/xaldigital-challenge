from data.item import Item
from typing import Optional
from network.http_request import HTTPRequest
from data.stack_overflow_data import StackOverflowData

STACK_OVERFLOW_API: str = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'

def main():
		# Hacemos la solicitud HTTP y obtenemos los datos JSON
		json_data = HTTPRequest().make_request('GET', STACK_OVERFLOW_API)

		# Convertimos los datos JSON a un objeto StackOverflowData utilizando la función from_json
		stack_overflow_data: StackOverflowData = StackOverflowData.from_json(json_data)

		# Utilizamos los métodos de la clase StackOverflowData según los requisitos especificados
		answered_count: int = stack_overflow_data.get_answered_count()
		unanswered_count: int = stack_overflow_data.get_unanswered_count()
		least_viewed_answer: Optional[Item] = stack_overflow_data.get_least_viewed_answer()
		oldest_answer: Optional[Item] = stack_overflow_data.get_oldest_answer()
		latest_answer: Optional[Item] = stack_overflow_data.get_latest_answer()
		answer_of_owner_highest_reputation: Optional[Item] = stack_overflow_data.get_answer_of_owner_with_highest_reputation()

		# Imprimimos los resultados
		print("Número de respuestas contestadas:", answered_count)
		print("\nNúmero de respuestas no contestadas:", unanswered_count)
		print("\nRespuesta con menor número de vistas:", least_viewed_answer)
		print("\nRespuesta más vieja:", oldest_answer)
		print("\nRespuesta más actual:", latest_answer)
		print("\nRespuesta del propietario con mayor reputación:", answer_of_owner_highest_reputation)

if __name__ == "__main__":
		main()