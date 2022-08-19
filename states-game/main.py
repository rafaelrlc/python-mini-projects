import time
import turtle

import pandas as pd

from scoreboard import *

states = pd.read_csv('50_states.csv')

image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title('US STATES GAME')
screen.addshape(image)
turtle.shape(image)



game_on = True
num_lifes = 3
num_score = 0
list_states = states['state'].to_list()
list_found_states = []


scoreboard_pontos = Scoreboard(-275, -230, "Score", num_score)
scoreboard_vidas = Scoreboard(-275, -200, "Lifes", num_lifes)

scoreboard_pontos.create_scoreboard()
scoreboard_vidas.create_scoreboard()
while game_on:
    valid = False
    guess = screen.textinput(title="Guess the State", prompt="What is the state name?").lower()

    for estados in states['state']:
        if guess == "exit":
            not_guessed = pd.DataFrame(list_states, columns=['States'])
            not_guessed.to_csv('states_remaning.csv')
            game_on = False
            break
        elif guess in list_found_states:
            print("State already guessed.")
            valid = True
            break
        elif guess == estados:
            print("Correct")
            valid = True
            list_states.remove(guess)
            list_found_states.append(guess)
            filter_state = (states['state'] == guess)
            x = int(states['x'][filter_state])
            y = int(states['y'][filter_state])
            name = turtle.Turtle()
            name.hideturtle()
            name.penup()
            name.goto(x, y)
            name.write(guess)
            scoreboard_pontos.score_inc()
            break

    if valid == False:
        scoreboard_vidas.score_inc()

    if scoreboard_vidas.score == 0:
        scoreboard_vidas.gameover('Lose')
        time.sleep(1.5)
        game_on = False

    if len(list_states) == 0:
        scoreboard_vidas.gameover('Win')
        game_on = False



