import unittest
from unittest.mock import patch
from Player import Player

class TestPlayer(unittest.TestCase):
    @patch('builtins.input', side_effect=['r', 'h'])
    def test_round_hold(self, mock_input):
        player = Player('John')
        player.round()
        self.assertEqual(player.roundscore, 0)
        self.assertEqual(player.playerscore, 0)

    @patch('builtins.input', side_effect=['r', 'r', 'h'])
    def test_round_score(self, mock_input):
        player = Player('Jane')
        player.round()
        self.assertGreater(player.roundscore, 0)
        self.assertGreaterEqual(player.playerscore, 0)


if __name__ == '__main__':
    unittest.main()
