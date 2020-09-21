from flask import render_template, request
from app import app
from app.models.RPS import *
# from app.models.game import Game
from app.models.RPS_game import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick-your-hand')
def pick_your_hand():
    return render_template('pickyourhand.html')

@app.route('/gameplay', methods=['POST'])
def play_the_game():
    player_1_name = request.form["player1"]
    player_1_choice = request.form["choices1"]
    player_2_name = request.form["player2"]
    player_2_choice = request.form["choices2"]
    player1 = Player(player_1_name, player_1_choice)
    player2 = Player(player_2_name, player_2_choice)
    gameplay(player1, player2)
    return render_template('pickyourhand.html', results=results)

@app.route('/')
def rules():
     return render_template('index.html')