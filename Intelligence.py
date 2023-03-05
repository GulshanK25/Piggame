# pylint: disable=import-error


from Dice import Die


class Intelligence:
    """
    Represents an intelligence that plays the game of Pig.

    Attributes:
        name (str): The name of the intelligence.
        roundscore (int): The score accumulated by the intelligence
          in the current round.
        computerscore (int): The total score accumulated by the intelligence.

    Methods:
        __init__(name): Initializes a new intelligence object
          with the given name and scores.
        __str__(): Returns the name of the intelligence as a string.
        round(): Simulates a round of the game of Pig for the intelligence.
    """
    def __init__(self, name):
        self.name = name
        self.roundscore = 0
        self.computerscore = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
        """
        Simulates a round of the game of Pig for the intelligence.
        If the score for this round is less than 20,
        the intelligence rolls a die and adds the value to the
        round score. If the die value is 1,
        the round score is reset to 0 and the turn ends. If the round score
        reaches 20 or more, the intelligence holds
        and adds the round score to the total score. The method
        calls itself recursively until the turn ends.
        """
        if self.roundscore < 20:
            roll = Die().value
            print(f"Computer rolls {roll}")
            if roll != 1:
                self.roundscore += roll
                print(f"Score for this round is  {self.roundscore}")
                self.round()
                self.roundscore = 0
            else:
                print("Sorry You Pigged!!!")
                self.round_score = 0
                self.computerscore += self.roundscore
                print(f"Total score for computer is {self.computerscore}")
        else:
            print("Computer holds")
            self.computerscore += self.roundscore
            print(f"Total score for computer is {self.computerscore}")
            self.roundscore = 0
