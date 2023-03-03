import unittest
from unittest.mock import patch
from Intelligence import Intelligence
#  from random import randint


class TestIntelligence(unittest.TestCase):
    def setUp(self):
        self.intelligence = Intelligence("Test")

    def test_init(self):
        self.assertEqual(self.intelligence.name, "Test")
        self.assertEqual(self.intelligence.roundscore, 0)
        self.assertEqual(self.intelligence.computerscore, 0)

    @patch('intelligence.Die.value', return_value=2)
    def test_round(self, mock_die):
        self.intelligence.round()
        self.assertEqual(self.intelligence.roundscore, 2)

    @patch('intelligence.Die.value', return_value=1)
    def test_round_rolls_one(self, mock_die):
        self.intelligence.round()
        self.assertEqual(self.intelligence.roundscore, 0)
        self.assertEqual(self.intelligence.computerscore, 0)

    @patch('intelligence.Die.value', return_value=2)
    def test_round_rolls_twenty(self, mock_die):
        self.intelligence.roundscore = 18
        self.intelligence.round()
        self.assertEqual(self.intelligence.roundscore, 0)
        self.assertEqual(self.intelligence.computerscore, 20)


if __name__ == '__main__':
    unittest.main()
