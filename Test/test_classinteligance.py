"""
Test class for the Intelligence class.
"""
import unittest
from unittest import mock
from unittest.mock import patch
from src.intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """
    Test class for the Intelligence class.
    """

    def test_init(self):
        """
        Test that the __init__() method initializes a new Intelligence object
        with the correct attributes.
        """
        intelligence = Intelligence("Computer")
        self.assertEqual(intelligence.name, "Computer")
        self.assertEqual(intelligence.roundscore, 0)
        self.assertEqual(intelligence.computerscore, 0)

    def test_str(self):
        """
        Test that the __str__() method returns the name of the intelligence
        as a string.
        """
        intelligence = Intelligence("Computer")
        self.assertEqual(str(intelligence), "Computer")

    @patch('src.dice.Die')
    def test_round(self, mock_dice):
        # Create a mock Die object with controlled roll values
        print(mock_dice)
        mock_die = mock.Mock()
        mock_die.value = 5

        # Create a new Intelligence object with the mock Die object
        intelligence = Intelligence("Computer")
        intelligence.roundscore = 0
        intelligence.computerscore = 0
        intelligence.round()

        # Check that the round score is updated correctly
        self.assertEqual(intelligence.roundscore, 0)

        # Mock a roll of 1 and test that the round score is reset to 0
        mock_die.value = 1
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        # Mock rolls of 2, 3, 4, and 5 to reach a score of 14
        mock_die.value = 2
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 3
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 4
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 5
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        # Mock a roll of 1 to reset the round score to 0
        mock_die.value = 1
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        # Mock rolls of 1, 2, 3, 4, and 5 to reach a score of 15
        mock_die.value = 1
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 2
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 3
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 4
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)

        mock_die.value = 5
        intelligence.round()
        self.assertEqual(intelligence.roundscore, 0)
