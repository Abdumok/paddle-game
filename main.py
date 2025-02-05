from turtle import Screen
from paddle import Paddle
from food import Food

# Setup the main Screen
window= Screen()
window.bgcolor("black")
window.setup(width= 1000, height= 600)
window.title("Paddle Game v1.00")
window.tracer(0)

# initialize the paddle:
paddle= Paddle()

# Control paddle movement:
window.listen()
window.onkey(fun=paddle.go_left, key="Left")
window.onkey(fun=paddle.go_right, key="Right")

# initialize food:
food = Food()
game_on= True
while game_on:



    window.update()
window.exitonclick()