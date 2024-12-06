import unittest
from fraction import *

class TestFraction(unittest.TestCase):

    def test_constructor(self):
        self.assertEqual(str(Fraction(4, 8)), "1/2")
        self.assertEqual(str(Fraction(-4, -8)), "1/2")
        self.assertEqual(str(Fraction(-4, 8)), "-1/2")
        with self.assertRaises(ValueError):  # Den 0
            Fraction(1, 0)

    def test_str_and_as_mixed_number(self):
        self.assertEqual(str(Fraction(3, 6)), "1/2")
        self.assertEqual(str(Fraction(3, 1)), "3")
        self.assertEqual(str(Fraction(2, -3)), "-2/3")
        self.assertEqual(str(Fraction(0, 4)), "0")

        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "1/2")

    def test_addition(self):
        self.assertEqual(Fraction(0, 1) + Fraction(1, 3), Fraction(1, 3))
        self.assertEqual(Fraction(0, 1) + Fraction(0, 1), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 3) + Fraction(-2, 3), Fraction(-1, 1))  # negatif + negatif
        self.assertEqual(Fraction(1, 2) + Fraction(2, 3), Fraction(7, 6))  # deux positifs
        self.assertEqual(Fraction(-1, 2) + Fraction(2, 3), Fraction(1, 6))  # negatif + positif

    def test_subtraction(self):
        self.assertEqual(Fraction(0, 1) - Fraction(1, 3), Fraction(-1, 3))
        self.assertEqual(Fraction(1, 3) - Fraction(0, 1), Fraction(1, 3))
        self.assertEqual(Fraction(-1, 2) - Fraction(-1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))  # positif - positif
        self.assertEqual(Fraction(1, 2) - Fraction(-1, 3), Fraction(5, 6))  # positif - neg
        self.assertEqual(Fraction(-1, 2) - Fraction(1, 3), Fraction(-5, 6))  # neg - positif

    def test_multiplication(self):
        self.assertEqual(Fraction(0, 1) * Fraction(1, 3), Fraction(0, 1))
        self.assertEqual(Fraction(1, 3) * Fraction(0, 1), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 2) * Fraction(0, 1), Fraction(0, 1))
        self.assertEqual(Fraction(4, 2) * Fraction(5, 1), Fraction(10, 1))
        self.assertEqual(Fraction(-4, 2) * Fraction(5, 1), Fraction(-10, 1))  # neg * positif
        self.assertEqual(Fraction(-4, 2) * Fraction(-5, 1), Fraction(10, 1))  # deux neg
        self.assertEqual(Fraction(1, 2) * Fraction(2, 3), Fraction(1, 3))  # proper * proper

    def test_division(self):
        self.assertEqual(Fraction(0, 1) / Fraction(1, 3), Fraction(0, 1))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 3) / Fraction(0, 1)  # Division par 0
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 1) / Fraction(0, 1)  # 0 / 0
        self.assertEqual(Fraction(4, 2) / Fraction(5, 1), Fraction(2, 5))
        self.assertEqual(Fraction(-4, 2) / Fraction(5, 1), Fraction(-2, 5))  # neg / positif
        self.assertEqual(Fraction(-4, 2) / Fraction(-5, 1), Fraction(2, 5))  # deux neg

    def test_power(self):
        self.assertEqual(Fraction(0, 1) ** Fraction(2, 1), Fraction(0, 1))
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 1) ** Fraction(-1, 1)  # 0^(-1)
        self.assertEqual(Fraction(1, 3) ** Fraction(0, 1), Fraction(1, 1))
        self.assertEqual(Fraction(-1, 2) ** Fraction(2, 1), Fraction(1, 4))  # neg^pair
        with self.assertRaises(ValueError):
            Fraction(-1, 2) ** Fraction(1, 2)  # racine négative

    def test_equality(self):
        self.assertTrue(Fraction(2, 3) == Fraction(4, 6))
        self.assertFalse(Fraction(2, 3) == Fraction(3, 4))

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(1, 3).is_zero())
        self.assertFalse(Fraction(-1, 2).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 4).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(2, 3).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertTrue(Fraction(-1, 7).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())
        self.assertFalse(Fraction(0, 1).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(2, 2).is_adjacent_to(Fraction(1, 3)))
        with self.assertRaises(TypeError):  # Cas `other` pas une Fraction
            Fraction(1, 2).is_adjacent_to(1)

# =============================================================
# ============== TEST SUPPLEMENTAIRES INVALIDES ===============
# =============================================================

    def test_invalid_addition(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "not a fraction"

    def test_invalid_subtraction(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) - 42

    def test_invalid_multiplication(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * None

    def test_invalid_division(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) / [1, 2]

    def test_invalid_power(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) ** "not a fraction"

    # Tests pour couvrir les calculs dans __pow__
    def test_fractional_exponent_complex_result(self):
        with self.assertRaises(ValueError):  # Racine négative
            Fraction(-2, 3) ** Fraction(1, 2)

    def test_fractional_exponent_non_integer_result(self):
        with self.assertRaises(ValueError):  # Fraction non représentable
            Fraction(2, 3) ** Fraction(1, 2)

    def test_integer_exponent(self):
        self.assertEqual(Fraction(2, 3) ** Fraction(2, 1), Fraction(4, 9))

    # Tests pour couvrir la méthode __float__
    def test_float_conversion(self):
        self.assertAlmostEqual(float(Fraction(1, 2)), 0.5)
        self.assertAlmostEqual(float(Fraction(-3, 4)), -0.75)
        self.assertEqual(float(Fraction(0, 1)), 0.0)

if __name__ == "__main__":
    unittest.main()