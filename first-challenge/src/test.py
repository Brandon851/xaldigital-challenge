import unittest
from data.item import Item
from data.owner import Owner
from data.stack_overflow_data import StackOverflowData

class TestStackOverflowData(unittest.TestCase):
		def setUp(self):
				# Creamos dos propietarios
				owner_1 = Owner(reputation=1000, user_id=1, user_type='registered', profile_image='', display_name='Brandon Fuentes', link='')
				owner_2 = Owner(reputation=50, user_id=2, user_type='registered', profile_image='', display_name='Juancho Gutierrez', link='')
				
				# Creamos tres items asociados a los propietarios
				item_1 = Item(tags=[], owner=owner_1, is_answered=True, view_count=10, answer_count=2, score=5, last_activity_date=0, creation_date=1234567891, last_edit_date=0, question_id=1, content_license='', link='', title='Ejemplo 1')
				item_2 = Item(tags=[], owner=owner_2, is_answered=False, view_count=2, answer_count=0, score=3, last_activity_date=0, creation_date=1234567892, last_edit_date=0, question_id=2, content_license='', link='', title='Ejemplo 2')
				item_3 = Item(tags=[], owner=owner_2, is_answered=False, view_count=8, answer_count=0, score=1, last_activity_date=0, creation_date=1234567893, last_edit_date=0, question_id=2, content_license='', link='', title='Ejemplo 3')
				
				# Creamos una instancia de StackOverflowData con los items
				self.stack_overflow_data = StackOverflowData([item_1, item_2, item_3], has_more=False, quota_max=100, quota_remaining=50)

		def test_get_answered_count(self):
				# Verificar si el número de respuestas contestadas es correcto
				self.assertEqual(self.stack_overflow_data.get_answered_count(), 1)

		def test_get_unanswered_count(self):
				# Verificar si el número de respuestas no contestadas es correcto
				self.assertEqual(self.stack_overflow_data.get_unanswered_count(), 2)

		def test_get_least_viewed_answer(self):
				# Verificar si la respuesta con menor número de vistas es correcta
				expected_title = 'Ejemplo 2'
				least_viewed_answer = self.stack_overflow_data.get_least_viewed_answer()
				self.assertEqual(least_viewed_answer.title, expected_title)

		def test_get_oldest_answer(self):
				# Verificar si la respuesta más vieja es correcta
				oldest_answer = self.stack_overflow_data.get_oldest_answer()
				self.assertIsNotNone(oldest_answer)
				expected_title = 'Ejemplo 1'
				self.assertEqual(oldest_answer.title, expected_title)

		def test_get_latest_answer(self):
				# Verificar si la respuesta más actual es correcta
				latest_answer = self.stack_overflow_data.get_latest_answer()
				self.assertIsNotNone(latest_answer)
				expected_title = 'Ejemplo 3'
				self.assertEqual(latest_answer.title, expected_title)

		def test_get_answer_of_owner_with_highest_reputation(self):
				# Verificar si la respuesta del propietario con mayor reputación es correcta
				answer_of_owner_highest_reputation = self.stack_overflow_data.get_answer_of_owner_with_highest_reputation()
				self.assertIsNotNone(answer_of_owner_highest_reputation)
				expected_owner_display_name = 'Brandon Fuentes'
				self.assertEqual(answer_of_owner_highest_reputation.owner.display_name, expected_owner_display_name)

if __name__ == '__main__':
		unittest.main()