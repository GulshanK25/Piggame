# pylint: disable=missing-module-docstring
import unittest
from unittest.mock import patch, MagicMock
from Game import Game
#  from Player import Player
#  from Intelligence import Intelligence


class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "Alice", "Bob"])
    def test_player_vs_player(self, mock_input):
        game = Game()
        game.letsstart()
        self.assertGreaterEqual(game.player.playerscore, 100)
        self.assertGreaterEqual(game.player2.playerscore, 100)
        self.assertIsNotNone(game.player.name)
        self.assertIsNotNone(game.player2.name)

    @patch('builtins.input', side_effect=["2", "Alice"])
    def test_player_vs_computer(self, mock_input):
        game = Game()
        game.computer = MagicMock()
        game.computer.computerscore = 100
        game.letsstart()
        self.assertGreaterEqual(game.computer.computerscore, 100)
        self.assertGreaterEqual(game.player.playerscore, 100)
        self.assertIsNotNone(game.player.name)


if __name__ == '__main__':
    unittest.main()
