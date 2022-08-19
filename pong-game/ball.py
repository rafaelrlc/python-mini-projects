from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10

    def create_ball(self):

        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(0, 0)
        initial_angle1 = random.randint(0, 15)
        self.setheading(initial_angle1)
        #self.first = True
        #if left_or_right == 1:
            #self.setheading(initial_angle1)
        #else:
            #self.setheading(initial_angle2)

    def move_ball(self):
        self.forward(25)

    #def move_ball_slower(self):
        #self.forward(10)
        #self.first = False

    def colision_botton(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def again(self):
        self.goto(0, 0)

#class Colision(Ball):
    #def __init__(self):
        #super().__init__()

    #def colion_botton(self):
        #if self.ycor() == 800:
            #print("ENCOSTOU")