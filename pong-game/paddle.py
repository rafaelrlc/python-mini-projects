from turtle import Turtle
from ball import Ball

class Padles(Ball):
    def __init__(self, x_inicial, y_inicial):

        super().__init__()
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.create_paddle()

    def create_paddle(self):

        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto((self.x_inicial, self.y_inicial))

    def up(self):
        novo_y = self.ycor() + 20
        self.goto(self.xcor(), novo_y)

    def down(self):
        novo_y = self.ycor() - 20
        self.goto(self.xcor(), novo_y)