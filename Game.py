<<<<<<< HEAD
from random import randint
#  from Dice import Die
from Player import Player
from Intelligence import Intelligence


class Game:
    def __init__(self):
        print("*****WELCOME TO THE GAME*********")
        print("Do you want to play as player vs player or player vs computer?")
        print("1. player vs player")
        print("2. player vs computer")
        self.opchoice = int(input("enter your choice :"))
        print("Rules For the game")
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
              "it becomes the next player's turn.")
        if self.opchoice == 1:
            self.player = Player(input("enter player1 name :"))
            self.player2 = Player(input("enter player2 name :"))
        else:
            self.computer = Intelligence("Computer")
            # intializing player for computer
            self.player = Player(input("enter players name :"))
            # intializing player name

    def letsstart(self):
        if self.opchoice == 2:
            playing = randint(1, 2)
            # deciding whether if computer or the player2 plays first
            if playing == 1:
                print("Computer goes first.")
                while (self.computer.computerscore < 100 and
                       self.player.playerscore < 100):
                    self.computer.round()  # playing for computer
                    if self.computer.computerscore == 100:
                        print("Computer wins!")
                        return
                    else:
                        self.player.round()  # playing for player
                if self.computer.computerscore >= 100:
                    print("Computer wins!")
                    return
                else:
                    print(f"{self.player} wins!")
                    return
            else:
                print(f"{self.player} goes first.")
                while (self.computer.computerscore < 100 and
                       self.player.playerscore < 100):
                    self.player.round()
                    # playing for player
                    if self.player.playerscore == 100:
                        print(f"{self.player} wins!")
                        return
                    else:
                        self.computer.round()
                if self.computer.computerscore >= 100:
                    print("Computer wins!")
                    return
                else:
                    print(f"{self.player} wins!")
                    return
        else:
            playing = randint(1, 2)
            # deciding whether if player1  or the player2 plays first
            if playing == 1:
                print(f"{self.player} plays first.")
                while (self.player.playerscore < 100 and
                        self.player2.playerscore < 100):
                    self.player.round()
                    # playing for player1
                    if self.player.playerscore == 100:
                        print(f"{self.player} wins!")
                        return
                    else:
                        self.player2.round()  # playing for player2
                if self.player.playerscore >= 100:
                    print(f"{self.player} wins!")
                    return
                else:
                    print(f"{self.player2} wins!")
                    return
            else:
                print(f"{self.player2} plays first.")
                while (self.player.playerscore < 100 and
                        self.player2.playerscore < 100):
                    self.player2.round()  # playing for player2
                    if self.player2.playerscore == 100:
                        print(f"{self.player2} wins!")
                        return
                    else:
                        self.player.round()  # playing for player1
                if self.player.playerscore >= 100:
                    print(f"{self.player} wins!")
                    return
                else:
                    print(f"{self.player2} wins!")
                    return
=======
from random import randint
#  from Dice import Die
from Player import Player
from Intelligence import Intelligence


class Game:
    def __init__(self):
        print("*****WELCOME TO THE GAME*********")
        print("Do you want to play as player vs player or player vs computer?")
        print("1. player vs player")
        print("2. player vs computer")
        self.opchoice = int(input("enter your choice :"))
        print("Rules For the game")
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
              "it becomes the next player's turn.")
        if self.opchoice == 1:
            self.player = Player(input("enter player1 name :"))
            self.player2 = Player(input("enter player2 name :"))
        else:
            self.computer = Intelligence("Computer")
            # intializing player for computer
            self.player = Player(input("enter players name :"))
            # intializing player name

    def letsstart(self):
        if self.opchoice == 2:
            playing = randint(1, 2)
            # deciding whether if computer or the player2 plays first
            if playing == 1:
                print("Computer goes first.")
                while (self.computer.computerscore < 100 and
                       self.player.playerscore < 100):
                    self.computer.round()  # playing for computer
                    if self.computer.computerscore == 100:
                        print("Computer wins!")
                        return
                    else:
                        self.player.round()  # playing for player
                if self.computer.computerscore >= 100:
                    print("Computer wins!")
                    return
                else:
                    print(f"{self.player} wins!")
                    return
            else:
                print(f"{self.player} goes first.")
                while (self.computer.computerscore < 100 and
                       self.player.playerscore < 100):
                    self.player.round()
                    # playing for player
                    if self.player.playerscore == 100:
                        print(f"{self.player} wins!")
                        return
                    else:
                        self.computer.round()
                if self.computer.computerscore >= 100:
                    print("Computer wins!")
                    return
                else:
                    print(f"{self.player} wins!")
                    return
        else:
            playing = randint(1, 2)
            # deciding whether if player1  or the player2 plays first
            if playing == 1:
                print(f"{self.player} plays first.")
                while (self.player.playerscore < 100 and
                        self.player2.playerscore < 100):
                    self.player.round()
                    # playing for player1
                    if self.player.playerscore == 100:
                        print(f"{self.player} wins!")
                        return
                    else:
                        self.player2.round()  # playing for player2
                if self.player.playerscore >= 100:
                    print(f"{self.player} wins!")
                    return
                else:
                    print(f"{self.player2} wins!")
                    return
            else:
                print(f"{self.player2} plays first.")
                while (self.player.playerscore < 100 and
                        self.player2.playerscore < 100):
                    self.player2.round()  # playing for player2
                    if self.player2.playerscore == 100:
                        print(f"{self.player2} wins!")
                        return
                    else:
                        self.player.round()  # playing for player1
                if self.player.playerscore >= 100:
                    print(f"{self.player} wins!")
                    return
                else:
                    print(f"{self.player2} wins!")
                    return
>>>>>>> 4f721cbdbca2fc8f95e5d45572956ff487f1bc27
