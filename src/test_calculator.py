import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calculator(10, 5, "add"), 15)

	def test_subtraction(self):
		self.assertEqual(calculator(10, 5, "subtract"), 5)

	def test_multiplication(self):
		self.assertEqual(calculator(10, 5, "multiply"), 50)

	def test_division(self):
		self.assertEqual(calculator(10, 5, "divide"), 2)

	def test_division_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			calculator(10, 0, "divide")

	def test_invalid_operation(self):
		with self.assertRaises(ValueError):
			calculator(10, 5, "invalid")


if __name__ == "__main__":
	unittest.main()
