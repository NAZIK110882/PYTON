"""Тести для math_utils.py за допомогою unittest."""
import unittest

from math_utils import add, divide, is_even, factorial


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(0, 7), 7)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


class TestDivide(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_fraction(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=4)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


class TestIsEven(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(4))

    def test_odd(self):
        self.assertFalse(is_even(7))

    def test_zero_and_negative(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))
        self.assertFalse(is_even(-3))

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            is_even("4")
        with self.assertRaises(TypeError):
            is_even(2.5)


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_five(self):
        self.assertEqual(factorial(5), 120)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            factorial(3.5)


if __name__ == "__main__":
    unittest.main()
