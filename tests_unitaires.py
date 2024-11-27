import unittest
from fraction import *


class TestFraction(unittest.TestCase):

    def test_initialization_and_simplification(self):
        self.assertEqual(str(Fraction(4, 8)), "1/2")
        self.assertEqual(str(Fraction(-4, -8)), "1/2")
        self.assertEqual(str(Fraction(-4, 8)), "-1/2")

    def test_string_representation(self):
        self.assertEqual(str(Fraction(3, 1)), "3")
        self.assertEqual(str(Fraction(3, 4)), "3/4")

    def test_mixed_number_representation(self):
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")

    def test_addition(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))

    def test_subtraction(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))

    def test_multiplication(self):
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))

    def test_division(self):
        self.assertEqual(Fraction(2, 3) / Fraction(3, 4), Fraction(8, 9))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_power(self):
        self.assertEqual(Fraction(2, 3) ** Fraction(2, 1), Fraction(4, 9))

    def test_equality(self):
        self.assertTrue(Fraction(2, 3) == Fraction(4, 6))

    def test_float_conversion(self):
        self.assertAlmostEqual(float(Fraction(1, 2)), 0.5)

    def test_properties(self):
        # Test is_zero
        self.assertTrue(Fraction(0, 3).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())
        # Test is_integer
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(1, 3).is_integer())
        # Test is_proper
        self.assertTrue(Fraction(2, 3).is_proper())
        self.assertFalse(Fraction(3, 1).is_proper())
        # Test is_unit
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(5, 3).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(2, 2).is_adjacent_to(Fraction(1, 3)))

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + 1


if __name__ == "__main__":
    unittest.main()
