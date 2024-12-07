class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : None
        POST : The fraction is initialized and simplified with GCD
        RAISES : if den = 0 then ValueError
        """


    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None.
        POST : Returns a string : 'num/den'.
        """

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None.
        POST : Returns a string : 'integer part + remainder/denominator'.
        """

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : None
        POST : Returns the sum with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : None
        POST : Returns the subtraction with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : None
        POST : Returns the multiplication with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : None
        POST : Returns the division with a new simplified Fraction.
        RAISES :
                - TypeError if `other` is not a Fraction instance.
                - ZeroDivisionError if `other` has a numerator of 0.
        """

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : None
        POST : Returns the power with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : None
        POST : Returns True if the fractions are equal, otherwise False.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None.
        POST : Returns a float number (the result of num / den).
        """

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None.
        POST : Returns True if num == 0, otherwise False.
        """

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None.
        POST : Returns True if the numerator is an exact multiple of the denominator.
        """

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None.
        POST : Returns True if the absolute value of the fraction is less than 1.
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None.
        POST : returns True if the numerator is 1.
        """

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        PRE : None
        POST : Returns True if the fractions differ by exactly 1/denominator.
        RAISES : TypeError if `other` is not a Fraction instance.
        """
