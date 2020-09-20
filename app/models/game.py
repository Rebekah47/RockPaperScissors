from app.models.RPS import *

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.results = []   

    def gameplay(self, player1, player2):
        if player1.choice == player2.choice:
             self.results.append("It's a draw.")
        elif player1.choice == "rock" and player2.choice == "paper":
            self.results.append(player2.name + " wins!")
        elif player2.choice == "rock" and player1.choice == "paper":
            self.results.append(player1.name + " wins!")
        elif player1.choice == "paper" and player2.choice == "scissors":
            self.results.append(player2.name + " wins!")
        elif player2.choice == "paper" and player2.choice == "scissors":
            self.results.append(player1.name + " wins!")
        elif player1.choice == "scissors" and player2.choice == "rock":
            self.results.append(player2.name + " wins!")
        elif player2.choice == "scissors" and player1.choice == "rock":
            self.results.append(player1.name + " wins!")


