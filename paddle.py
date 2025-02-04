from turtle import Turtle
START_POS= [(-45, -280) ,(-35, -280) ,(-25, -280), (-15, -280), (-5, -280), (5, -280), (15, -280), (25, -280),
            (35, -280), (45, -280)]

class Paddle:
    def __init__(self):
        self.paddle= []
        self.create_paddle()

    def create_paddle(self):
        for i in range(len(START_POS)):
            new_part = Turtle()
            new_part.color("white")
            new_part.shape("square")
            new_part.penup()
            new_part.shapesize(0.5)
            new_part.goto(START_POS[i])
            self.paddle.append(new_part)