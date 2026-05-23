import unittest
from math_utils import add, subtract, multiply, divide

class TestMathUtilsUnittest(unittest.TestCase):

    # тесты для add
    def test_add_success(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add(2, [1, 2])
        with self.assertRaises(TypeError):
            add(True, 5)

    # тесты для subtract 
    def test_subtract_success(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_subtract_type_error(self):
        with self.assertRaises(TypeError):
            subtract("5", 3)
        with self.assertRaises(TypeError):
            subtract(5, None)

    # тесты для multiply 
    def test_multiply_success(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0.5, 2), 1.0)

    def test_multiply_type_error(self):
        with self.assertRaises(TypeError):
            multiply("2", 3)

    # тесты для divide 
    def test_divide_success(self):
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0.0)

    def test_divide_type_error(self):
        with self.assertRaises(TypeError):
            divide("6", 3)

if __name__ == "__main__":
    unittest.main()