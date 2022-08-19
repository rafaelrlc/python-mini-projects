from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self,placar_x,placar_y,score_type,score_number):
        super().__init__()
        self.score = score_number
        self.positions_x = placar_x
        self.position_y = placar_y
        self.score_type = score_type

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.goto(self.positions_x, self.position_y)
        self.write(f"{self.score_type}: {self.score}", move=False, align='center', font=('Courier', 15, 'normal'))
        self.hideturtle()

    def delete_scoreboard(self):
        self.clear()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=('Courier', 15, 'normal'))

    def score_inc(self):
        if self.score_type == "Vidas":
            self.score = self.score - 1

        elif self.score_type == "Pontos":
            self.score = self.score + 1

        self.delete_scoreboard()
        self.create_scoreboard()