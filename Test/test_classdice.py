# pylint: disable=import-error

import unittest
#  from unittest.mock import patch
from src.dice import Die


class TestDie(unittest.TestCase):
    """
    A test class for the Die class.

    Attributes:
        None

    Methods:
        test_init: Test the initialization of a new die object.
        test_str: Test the string representation of a die object.
    """

    def test_init(self):
        """
        Test the initialization of a new die object.
        """
        die = Die()
        self.assertIn(die.value, range(1, 7))

    def test_str(self):
        """
        Test the string representation of a die object.
        """
        die = Die()
        self.assertEqual(str(die), str(die.value))


if __name__ == '__main__':
    unittest.main()
