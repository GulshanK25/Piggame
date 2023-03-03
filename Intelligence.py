from Dice import Die


class Intelligence:
    def __init__(self, name):
        self.name = name
        self.roundscore = 0
        self.computerscore = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
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
