# pylint: disable=import-error

import unittest
from unittest.mock import patch
from Dice import Die


class TestDie(unittest.TestCase):
    """
    A test case class for the Die class.
    """

    @patch('die.randint', return_value=2)
    def test_init(self, mock_randint):
        """
        Test the initialization of the Die object.

        Mocks the `randint` function
        from the `random` module to always return 2,
        and checks that the `value` attribute of the Die object is set to 2.
        """
        die = Die()
        self.assertEqual(die.value, 2)

    def test_str(self):
        """
        Test the string representation of the Die object.

        Creates a Die object and
        checks that the string representation of the object
        is equal to the string representation of the `value` attribute
        of the object.
        """
        die = Die()
        self.assertEqual(str(die), str(die.value))


if __name__ == '__main__':
    unittest.main()
