import random
import time
from turtle import Turtle, Screen
from paddle import Padles
from scoreboard import Scoreboard
from ball import Ball


#CREATE SCRREN
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#SETAR NUMERO DE VIDAS
VIDAS = 5
#PADDLE 1
p1 = Padles(350, 0)
#PADDLE 2
p2 = Padles(-350, 0)
#SET SCOREBOARD's
scoreboard = Scoreboard(0, 270, "Pontos", 0)
lives_scoreboard = Scoreboard(0, -270, "Vidas", VIDAS)
scoreboard.create_scoreboard()
lives_scoreboard.create_scoreboard()
#SET SCREEN
screen.listen()
screen.onkeypress(p1.up, "Up")
screen.onkeypress(p1.down, "Down")
screen.onkeypress(p2.up, "w")
screen.onkeypress(p2.down, "s")
#SET BALL
ball = Ball()
ball.create_ball()

game = True
#GAME RUNNING
while game:
    #GAME OVER
    if lives_scoreboard.score == 0:
        scoreboard.gameover()
        break

    time.sleep(0.09)
    screen.update()
    ball.move_ball()
    #detectar colisao com teto
    if ball.ycor() < -273 or ball.ycor() > 273:
        ball.colision_botton()

    #detectar colisao com paddle
    if ball.distance(p1) < 50 and ball.xcor() > 330 or ball.distance(p2) < 50 and ball.xcor() < -330:
        angulo_atual = ball.heading()
        angulo_atual = angulo_atual + 180
        angulo_atual_menos = angulo_atual - 30

        angulo_ir = random.randint(angulo_atual_menos, angulo_atual)
        ball.setheading(angulo_ir)
        scoreboard.score_inc()

    #detectar colisao com a parede
    if ball.xcor() >= 380 and ball.xcor() <= 400 or ball.xcor() <= -380 and ball.xcor() >= -400:
        time.sleep(1)
        ball.again()
        lives_scoreboard.score_inc()


screen.exitonclick()