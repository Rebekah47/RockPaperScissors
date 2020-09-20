from app.models.RPS import *
from app.models.game import *

results = []

def clear_results():
    results.clear()

def gameplay(player1, player2):
    clear_results()
    if player1.choice == player2.choice:
        results.append("It's a draw.")
    elif player1.choice == "rock" and player2.choice == "paper":
        results.append(player2.name + " wins!")
    elif player2.choice == "rock" and player1.choice == "paper":
        results.append(player1.name + " wins!")
    elif player1.choice == "paper" and player2.choice == "scissors":
        results.append(player2.name + " wins!")
    elif player2.choice == "paper" and player2.choice == "scissors":
        results.append(player1.name + " wins!")
    elif player1.choice == "scissors" and player2.choice == "rock":
        results.append(player2.name + " wins!")
    elif player2.choice == "scissors" and player1.choice == "rock":
        results.append(player1.name + " wins!")

