# pylint: disable=too-few-public-methods
""" this is the dice class """
from random import randint


class Die:
    """
    Represents a die with a random value between 1 and 6.

    Attributes:
        value (int): The current value of the die.

    Methods:
        __init__(): Initializes a new die object with a random value.
        __str__(): Returns the string representation of the die's current
          value.
    """

    def __init__(self):
        self.value = randint(1, 6)

    def __str__(self):
        return f"{self.value}"
