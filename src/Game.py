# pylint: disable=missing-class-docstring
""" this is the game played class """
#  from Dice import Die
from src.player import Player
from src.intelligence import Intelligence


class Game:
    """ Represents a game of Pig."""

    def __init__(self):
        self.winner = ""
        print("*****WELCOME TO THE GAME*********\n")
        print("Do you want to play as player vs player or player vs computer?")
        print("1. player vs player")
        print("2. player vs computer\n")
        self.opchoice = input("enter your choice :")
        print("\n*************Rules For the game*************")
        print("1. The game is played with a single six-sided die.")
        print("2. At any time during a player's turn, "
              "the player is faced with two decisions:")
        print("   a. Roll the die again and"
              "add this number to his turn total.")
        print("   b. Hold and bank his turn total into his score."
              "After the player's turn is over,"
              "it becomes the next player's turn.")
        print("3. The first player to score 100 or more points wins.")
        print("4. If a player rolls a 1, he scores nothing and"
              "it becomes the next player's turn.\n")
        if self.opchoice == "1":
            self.player = Player(input("enter player1 name :"))
            self.player2 = Player(input("enter player2 name :"))
        else:
            self.computer = Intelligence("Computer")
            # intializing player for computer
            self.player = Player(input("enter players name :"))
            # intializing player name

    def __str__(self):
        return f"{self}"

    def letsstart(self):
        """ Represents the round of pig game where the players and
            the computer plays the rounds."""
        if self.opchoice == "2":
            print("Computer goes first.\n")
            while (self.computer.computerscore < 100 and
                    self.player.playerscore < 100):
                print("Computers turn\n ")
                self.computer.round()  # playing for computer
                if self.computer.computerscore == 100:
                    print("Computer wins!")
                    return
                print(f"{self.player} turn! \n.")
                self.player.round()  # playing for player
            self.winner = self.player if self.player.playerscore >= 100\
                else self.computer
        else:
            playing = int(input("1. for player1 \n 2. for player2\n"))
            # deciding whether if player1  or the player2 plays first
            if playing == 1:
                print(f"{self.player} plays first.\n")
                while (self.player2.playerscore < 100 and
                       self.player.playerscore < 100):
                    print(f"{self.player} turn! \n.")
                    self.player.round()  # playing for player1
                    if self.player.playerscore == 100:
                        print(f"{self.player} wins!")
                        return
                    print(f"{self.player2} turn! \n.")
                    self.player2.round()  # playing for player2
                self.winner = self.player if self.player.playerscore >= 100\
                    else self.player2
            else:
                print(f"{self.player2} plays first.")
                while (self.player2.playerscore < 100 and
                       self.player.playerscore < 100):
                    print(f"{self.player2} turn! \n.")
                    self.player2.round()  # playing for player2
                    if self.player2.playerscore == 100:
                        print(f"{self.player2} wins!")
                        return
                    print(f"{self.player} turn! \n.")
                    self.player.round()  # playing for player1
                self.winner = self.player if self.player.playerscore >= 100\
                    else self.player2

        print(f"{self.winner} wins!")
