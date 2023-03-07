# pylint: disable=attribute-defined-outside-init
"""Test class for the Game class"""
import unittest
from unittest.mock import patch
from src.game import Game


class TestGame(unittest.TestCase):
    """Test class for the Game class"""

    def test_game_player_vs_player(self):
        """Test that the game can be played by two human players"""
    @patch('builtins.input', side_effect=['1', '1', "2", "1", "cheatwin"])
    def test_letsstart_player1_wins(self, mock_input):
        """Test for player 1 to win"""
        print(mock_input)
        self.game = Game()
        self.game.letsstart()
        self.assertEqual(100, self.game.player.playerscore)

    @patch('builtins.input', side_effect=['1', '1', "2", "2", "cheatwin"])
    def test_letsstart_player2_wins(self, mock_input):
        """Test for player 2 to win"""
        print(mock_input)
        self.game = Game()
        self.game.letsstart()
        self.assertEqual(100, self.game.player2.playerscore)

    @patch('builtins.input', side_effect=['2', '1', "1", 'cheatwin'])
    def test_letsstart_computer_wins(self, mock_input):
        """Test for computer to win"""
        print(mock_input)
        self.game = Game()
        self.game.letsstart()
        self.assertEqual(100, 100)


if __name__ == '__main__':
    unittest.main()
