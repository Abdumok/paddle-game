from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x= -440, y= 280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Times New Roman", 12, "bold"), align="center")

    def increase(self, point):
        self.score += (1 * point)
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER \nYour Final Score: {self.score}", font=("Times New Roman", 22, "bold"), align="center")

