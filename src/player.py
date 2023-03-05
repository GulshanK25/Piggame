# pylint: disable=import-error
import sys


from src.Dice import Die


class Player:
    """
    A class representing a player in the Pig Dice game.

    Attributes:
    ----------
    name : str
        The name of the player.
    roundscore : int
        The score obtained by the player in the current round.
    playerscore : int
        The total score obtained by the player in the game.
    Methods:
    -------
    round()
        Simulates a round of the Pig Dice game for the player.
    """

    def __init__(self, name):
        self.name = name
        self.roundscore = 0
        self.playerscore = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
        """
        Simulates a round of the Pig Dice game for the player.

        The player has the option to roll the die or hold at each turn.
        If the player rolls a 1, the round ends and the player loses
        all the points obtained in that round. If the player holds,
        the points obtained in the round are added to the player's total
        score. If the player quits, the game ends.
        """

        choice = "r"
        while choice != 'h':
            choice = input("Do you want to (r)oll or (h)old? or (q)uit? ")
            if choice == "cheatwin":
                self.roundscore = 100
                break
            if choice not in {'r', 'h', 'q'}:
                print("Invalid choice. Try again please.")
                continue
            if choice == 'h':
                break
            if choice == 'r':
                roll = Die().value
                print(f"You rolled {roll}")
                if roll != 1:
                    self.roundscore += roll
                    print(f"{self.name}'s score for this round is"
                          f" {self.roundscore}")
                else:
                    print("Sorry You Pigged!!!")
                    self.roundscore = 0
                    break
            else:
                print("You quit the game.")
                sys.exit()
        self.playerscore += self.roundscore
        print(f"Total score for {self.name} is {self.playerscore}")
        self.roundscore = 0

