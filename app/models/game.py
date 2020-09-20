from app.models.RPS import *

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2   

def gameplay(self, player1, player2):
        if player1.choice == player2.choice:
            return "It's a draw."
        elif player1.choice == "rock" and player2.choice == "paper":
            return player2.name + " wins!"
        elif player2.choice == "rock" and player1.choice == "paper":
            return player1.name + " wins!"
        elif player1.choice == "paper" and player2.choice == "scissors":
            return player2.name + " wins!"
        elif player2.choice == "paper" and player2.choice == "scissors":
            return player1.name + " wins"
        elif player1.choice == "scissors" and player2.choice == "rock":
            return player2.name + " wins!"
        elif player2.choice == "scissors" and player1.choice == "rock":
            return player1.name + " wins!"