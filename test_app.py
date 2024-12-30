import unittest
from calc import app, arithmetic


class ArithmeticTests(unittest.TestCase):
    """Тести для класу Arithmetic"""

    def test_add(self):
        self.assertEqual(arithmetic.add(2, 3), 5)
        self.assertEqual(arithmetic.add(-1, 1), 0)
        self.assertEqual(arithmetic.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(arithmetic.subtract(5, 3), 2)
        self.assertEqual(arithmetic.subtract(0, 5), -5)
        self.assertEqual(arithmetic.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(arithmetic.multiply(4, 3), 12)
        self.assertEqual(arithmetic.multiply(-1, 5), -5)
        self.assertEqual(arithmetic.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(arithmetic.divide(6, 2), 3.0)
        self.assertEqual(arithmetic.divide(-6, -2), 3.0)
        with self.assertRaises(ValueError):
            arithmetic.divide(5, 0)


class FlaskAppTests(unittest.TestCase):
    """Тести для Flask-додатку"""

    def setUp(self):
        # Створюємо тестовий клієнт Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        # Перевіряємо, чи завантажується головна сторінка
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"form", response.data)  # Перевіряємо наявність форми в HTML

    def test_calculate_add(self):
        response = self.app.post('/calculate', data={'a': '3', 'b': '4', 'operation': 'add'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'7.0', response.data)

    def test_calculate_subtract(self):
        response = self.app.post('/calculate', data={'a': '10', 'b': '4', 'operation': 'subtract'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'6.0', response.data)

    def test_calculate_multiply(self):
        response = self.app.post('/calculate', data={'a': '2', 'b': '3', 'operation': 'multiply'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'6.0', response.data)

    def test_calculate_divide(self):
        response = self.app.post('/calculate', data={'a': '8', 'b': '2', 'operation': 'divide'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'4.0', response.data)

    def test_calculate_divide_by_zero(self):
        response = self.app.post('/calculate', data={'a': '8', 'b': '0', 'operation': 'divide'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot divide by zero', response.data)

    def test_calculate_invalid_input(self):
        response = self.app.post('/calculate', data={'a': 'invalid', 'b': '2', 'operation': 'add'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input', response.data)


if __name__ == '__main__':
    unittest.main()
