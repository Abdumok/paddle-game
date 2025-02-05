import random
from turtle import Turtle

COLOR= ["white", "blue", "yellow", "red", "green"]
SHAPE= ["turtle", "square", "circle", "triangle"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        XCOR = random.randint(-480, 480)
        self.color(random.choice(COLOR))
        self.shape(random.choice(SHAPE))
        self.penup()
        self.goto(XCOR, 320)

    def move(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def hide(self):
        self.clear()



