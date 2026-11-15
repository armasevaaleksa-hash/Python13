import unittest
from lab13 import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    """Тести"""

    def test_add(self):
        """Перевірка"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)

    def test_divide_by_zero(self):
        """Перевірка обробки помилки при діленні на нуль"""
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
