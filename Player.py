from Dice import Die


class Player:
    def __init__(self, name):
        self.name = name
        self.roundscore = 0
        self.playerscore = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
        choice = "r"
        while choice != 'h':
            choice = input("Do you want to (r)oll or (h)old? or (q)uit? ")
            #  giving options to the player to roll or hold or quit the game
            if choice == "cheatwin":  # cheat code for the game
                self.roundscore = 100
                break
            if choice != 'r' and choice != 'h' and choice != 'q':
                print("Invalid choice. Try again.")
                continue
            if choice == 'h':
                break
            elif choice == 'r':
                roll = Die().value
                print(f"You rolled {roll}")
                if roll != 1:
                    self.roundscore += roll
                    print(f"{self.name}'s score for this round is {self.roundscore}")
                    # printing out the score
                else:
                    print("Sorry You Pigged!!!")
                    self.roundscore = 0
                    break
            else:
                print("You quit the game.")
                exit()
        self.playerscore += self.roundscore
        print(f"Total score for {self.name} is {self.playerscore}")
        self.roundscore = 0
