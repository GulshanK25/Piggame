import unittest
from unittest.mock import patch
from src.player import Player


class TestPlayer(unittest.TestCase):
    """" this is the test class for player"""

    @patch('builtins.input', side_effect=['r', 'h'])
    def test_round_hold(self, mock_input):
        """" this is the test class for player to hold"""
        print(mock_input)
        player = Player('John')
        player.round()
        self.assertEqual(player.roundscore, 0)
        self.assertGreaterEqual(player.playerscore, 0)

    @patch('builtins.input', side_effect=['r', 'r', 'h'])
    def test_round_score(self, mock_input):
        """" this is the test class for player to socre"""
        print(mock_input)
        player = Player('Jane')
        player.round()
        self.assertGreaterEqual(player.playerscore, 0)


if __name__ == '__main__':
    unittest.main()
