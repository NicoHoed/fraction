from math import gcd

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
        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = gcd(num, den)                 # Simplify fraction with GCD
        self.__numerator = num // common_divisor
        self.__denominator = den // common_divisor

        if self.denominator < 0:                     # Force den to be positive
            self.__numerator = -self.numerator
            self.__denominator = -self.denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None.
        POST : Returns a string : 'num/den'.
        """

        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None.
        POST : Returns a string : 'integer part + remainder/denominator'.
        """
        integer_part = self.numerator // self.denominator          # `//` give the integer part
        remainder = abs(self.numerator % self.denominator)         # `%` give the remainder

        if remainder == 0:
            return str(integer_part)
        elif integer_part == 0:
            return f"{remainder}/{self.denominator}"
        else:
            return f"{integer_part} {remainder}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : None
        POST : Returns the sum with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if not isinstance(other, Fraction):
            raise TypeError("Can only add two Fraction instances.")

        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator  # fraction sum formula
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : None
        POST : Returns the subtraction with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if not isinstance(other, Fraction):
            raise TypeError("Can only add two Fraction instances.")

        new_num = self.numerator * other.denominator - self.denominator * other.numerator
        new_den = self.denominator * other.denominator    # fraction sub. formula
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : None
        POST : Returns the multiplication with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if not isinstance(other, Fraction):
            raise TypeError("Can only add two Fraction instances.")

        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator    # fraction mul. formula
        return Fraction(new_num, new_den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : None
        POST : Returns the division with a new simplified Fraction.
        RAISES :
                - TypeError if `other` is not a Fraction instance.
                - ZeroDivisionError if `other` has a numerator of 0.
        """

        if not isinstance(other, Fraction):
            raise TypeError("Can only divide two Fraction instances.")

        if other.numerator == 0:
            raise ZeroDivisionError("Numerator cant be 0.")

        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator  # fraction division formula
        return Fraction(new_num, new_den)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : None
        POST : Returns the power with a new simplified Fraction.
        RAISES :
            - TypeError if `other` is not a Fraction instance.
            - ValueError if the result would be a complex number or non-representable fraction.
        """

        if not isinstance(other, Fraction):
            raise TypeError("Can only power two Fraction instances.")

        if self.numerator < 0:  # Negative base with fractional exponent
            raise ValueError("Cannot calculate the fractional power of a negative number.")

        if other.denominator == 1:  # Exponent is an integer
            num_power = pow(self.numerator, other.numerator)
            den_power = pow(self.denominator, other.numerator)
            return Fraction(num_power, den_power)

        # Handle fractional exponents
        num_power = pow(self.numerator, other.numerator)
        den_power = pow(self.denominator, other.numerator)

        num_result = num_power ** (1 / other.denominator)
        den_result = den_power ** (1 / other.denominator)

        # Ensure results are integers for valid fractions by rounding and comparing
        if round(num_result) != num_result or round(den_result) != den_result:
            raise ValueError("Resulting fraction is not representable as integers.")

        return Fraction(int(round(num_result)), int(round(den_result)))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : None
        POST : Returns True if the fractions are equal, otherwise False.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            raise TypeError("Can only compare two Fraction instances.")

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None.
        POST : Returns a float number (the result of num / den).
        """

        return self.numerator / self.denominator  # converts fraction to decimal

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None.
        POST : Returns True if num == 0, otherwise False.
        """

        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None.
        POST : Returns True if the numerator is an exact multiple of the denominator.
        """

        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None.
        POST : Returns True if the absolute value of the fraction is less than 1.
        """

        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None.
        POST : returns True if the numerator is 1.
        """

        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        PRE : None
        POST : Returns True if the fractions differ by exactly 1/denominator.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            return (self - other).is_unit()
        else:
            raise TypeError("Can only compare two Fraction instances.")