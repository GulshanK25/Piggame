<<<<<<< HEAD
import unittest
from unittest.mock import patch
from Dice import Die


class TestDie(unittest.TestCase):
    @patch('die.randint', return_value=2)
    def test_init(self, mock_randint):
        die = Die()
        self.assertEqual(die.value, 2)

    def test_str(self):
        die = Die()
        self.assertEqual(str(die), str(die.value))


if __name__ == '__main__':
    unittest.main()
=======
import unittest
from unittest.mock import patch
from Dice import Die


class TestDie(unittest.TestCase):
    @patch('die.randint', return_value=2)
    def test_init(self, mock_randint):
        die = Die()
        self.assertEqual(die.value, 2)

    def test_str(self):
        die = Die()
        self.assertEqual(str(die), str(die.value))


if __name__ == '__main__':
    unittest.main()
>>>>>>> 4f721cbdbca2fc8f95e5d45572956ff487f1bc27
