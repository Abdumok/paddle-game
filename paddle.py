from turtle import Turtle
START_POS= [(-45, -280) ,(-35, -280) ,(-25, -280), (-15, -280), (-5, -280), (5, -280), (15, -280), (25, -280),
            (35, -280), (45, -280)]

class Paddle:
    def __init__(self):
        self.all_parts= []
        self.create_paddle()

    def create_paddle(self):
        for i in range(len(START_POS)):
            new_part = Turtle()
            new_part.color("white")
            new_part.shape("square")
            new_part.penup()
            new_part.shapesize(0.5)
            new_part.goto(START_POS[i])
            self.all_parts.append(new_part)

    def go_left(self):
        # limit the paddle left movement:
        paddle_left_side= self.all_parts[0].xcor()
        if paddle_left_side > -460:
            for part in self.all_parts:
                part.goto(part.xcor() - 60, part.ycor())

    def go_right(self):
        # limit the paddle right movement:
        paddle_right_side= self.all_parts[-1].xcor()
        if paddle_right_side < 460:
            for part in self.all_parts:
                part.goto(part.xcor() + 60, part.ycor())