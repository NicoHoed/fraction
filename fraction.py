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

        if self.__denominator < 0:                     # Force den to be positive
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

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

        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return f"{self.__numerator}/{self.__denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None.
        POST : Returns a string : 'integer part + remainder/denominator'.
        """
        integer_part = self.__numerator // self.__denominator          # `//` give the integer part
        remainder = abs(self.__numerator % self.__denominator)         # `%` give the remainder

        if remainder == 0:
            return str(integer_part)
        elif integer_part == 0:
            return f"{remainder}/{self.__denominator}"
        else:
            return f"{integer_part} {remainder}/{self.__denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : `other` must be an instance of Fraction.
        POST : Returns the sum with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            new_num = self.__numerator * other.__denominator + self.__denominator * other.__numerator
            new_den = self.__denominator * other.__denominator    # fraction sum formula
            return Fraction(new_num, new_den)
        else:
            raise TypeError("Can only add two Fraction instances.")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : `other` must be an instance of Fraction.
        POST : Returns the subtraction with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            new_num = self.__numerator * other.__denominator - self.__denominator * other.__numerator
            new_den = self.__denominator * other.__denominator    # fraction sub. formula
            return Fraction(new_num, new_den)
        else:
            raise TypeError("Can only subtract two Fraction instances.")

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : `other` must be an instance of Fraction.
        POST : Returns the multiplication with a new simplified Fraction.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            new_num = self.__numerator * other.__numerator
            new_den = self.__denominator * other.__denominator    # fraction mul. formula
            return Fraction(new_num, new_den)
        else:
            raise TypeError("Can only multiply two Fraction instances.")

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : `other` must be an instance of Fraction.
        POST : Returns the division with a new simplified Fraction.
        RAISES :
                - TypeError if `other` is not a Fraction instance.
                - ZeroDivisionError if `other` has a numerator of 0.
        """

        if not isinstance(other, Fraction):
            raise TypeError("Can only divide two Fraction instances.")

        if other.__numerator == 0:
            raise ZeroDivisionError("Numerator cant be 0.")

        new_num = self.__numerator * other.__denominator
        new_den = self.__denominator * other.__numerator  # fraction division formula
        return Fraction(new_num, new_den)

    from math import isclose

    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : `other` must be an instance of Fraction.
        POST : Returns the power with a new simplified Fraction.
        RAISES :
            - TypeError if `other` is not a Fraction instance.
            - ValueError if the result would be a complex number or non-representable fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only power two Fraction instances.")

        if other.denominator == 1:  # Exponent is an integer
            num_power = pow(self.__numerator, other.numerator)
            den_power = pow(self.__denominator, other.numerator)
            return Fraction(num_power, den_power)

        if self.numerator < 0:  # Negative base with fractional exponent
            raise ValueError("Cannot compute the fractional power of a negative number.")

        # Handle fractional exponents
        num_power = pow(self.__numerator, other.numerator)
        den_power = pow(self.__denominator, other.numerator)

        num_result = num_power ** (1 / other.denominator)
        den_result = den_power ** (1 / other.denominator)

        # Ensure results are integers for valid fractions by rounding and comparing
        if round(num_result) != num_result or round(den_result) != den_result:
            raise ValueError("Resulting fraction is not representable as integers.")

        return Fraction(int(round(num_result)), int(round(den_result)))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : `other` must be an instance of Fraction.
        POST : Returns True if the fractions are equal, otherwise False.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator == self.__denominator * other.__numerator
        else:
            raise TypeError("Can only compare two Fraction instances.")

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None.
        POST : Returns a float number (the result of num / den).
        """

        return self.__numerator / self.__denominator  # converts fraction to decimal

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None.
        POST : Returns True if num == 0, otherwise False.
        """

        return self.__numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None.
        POST : Returns True if the numerator is an exact multiple of the denominator.
        """

        return self.__numerator % self.__denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None.
        POST : Returns True if the absolute value of the fraction is less than 1.
        """

        return abs(self.__numerator) < self.__denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None.
        POST : returns True if the numerator is 1.
        """

        return abs(self.__numerator) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        PRE : `other` must be an instance of Fraction.
        POST : Returns True if the fractions differ by exactly 1/denominator.
        RAISES : TypeError if `other` is not a Fraction instance.
        """

        if isinstance(other, Fraction):
            return (self - other).is_unit()
        else:
            raise TypeError("Can only compare two Fraction instances.")

# if __name__ == '__main__':
#    # Test initialisation et simplification
#    print(Fraction(4, 8))  # Doit afficher "1/2"
#    print(Fraction(-4, -8))  # Doit afficher "1/2"
#    print(Fraction(-4, 8))  # Doit afficher "-1/2"

#    print('---------------------------------------------------------------')

#    # Test représentation textuelle
#    print(Fraction(3, 1))  # Doit afficher "3"
#    print(Fraction(3, 4))  # Doit afficher "3/4"

#    print('---------------------------------------------------------------')

#    # Test représentation en nombre mixte
#    print(Fraction(7, 3).as_mixed_number())  # Doit afficher "2 1/3"
#    print(Fraction(4, 2).as_mixed_number())  # Doit afficher "2"

#    print('---------------------------------------------------------------')

#    # Test addition
#    print(Fraction(1, 2) + Fraction(1, 3))  # Doit afficher "5/6"
#    # Test soustraction
#    print(Fraction(1, 2) - Fraction(1, 3))  # Doit afficher "1/6"
#    # Test multiplication
#    print(Fraction(2, 3) * Fraction(3, 4))  # Doit afficher "1/2"
#    # Test division
#    print(Fraction(2, 3) / Fraction(3, 4))  # Doit afficher "8/9"

#    print('---------------------------------------------------------------')

#    # Test division par zéro
#    try:
#        print(Fraction(1, 2) / Fraction(0, 1))
#    except ZeroDivisionError as e:
#        print("Erreur détectée :", e)  # Doit afficher une erreur de division par zéro

#    print('---------------------------------------------------------------')

#    # Test puissance
#    print(Fraction(2, 3) ** Fraction(2, 1))  # Doit afficher "4/9"

#    print('---------------------------------------------------------------')

#    # Test égalité
#    print(Fraction(2, 3) == Fraction(4, 6))  # Doit afficher "True"

#    print('---------------------------------------------------------------')

#    # Test conversion en flottant
#    print(float(Fraction(1, 2)))  # Doit afficher "0.5"

#    print('---------------------------------------------------------------')

#    # Test propriétés
#    print(Fraction(0, 3).is_zero())  # Doit afficher "True"
#    print(Fraction(4, 2).is_integer())  # Doit afficher "True"
#    print(Fraction(2, 3).is_proper())  # Doit afficher "True"
#    print(Fraction(1, 3).is_unit())  # Doit afficher "True"
#    print('\n')
#    print(Fraction(1, 2).is_zero())  # Doit afficher "False"
#    print(Fraction(1, 3).is_integer())  # Doit afficher "False"
#    print(Fraction(3, 1).is_proper())  # Doit afficher "False"
#    print(Fraction(5, 3).is_unit())  # Doit afficher "False"

#    print('---------------------------------------------------------------')

#    # Test fraction adjacente
#    print(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))  # Doit afficher "True"
#    print(Fraction(2, 2).is_adjacent_to(Fraction(1, 3)))  # Doit afficher "False"

#    print('---------------------------------------------------------------')

#    # Test erreurs de type
#    try:
#        print(Fraction(1, 2) + 1)
#    except TypeError as e:
#        print("Erreur détectée :", e)  # Doit afficher une erreur de type
