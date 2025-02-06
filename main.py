from turtle import Screen
from paddle import Paddle
from food import Food
import time
from scorebord import Score

# Set up the main Screen
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

score= Score()


game_on= True
while game_on:
    if food.ycor() > -380:
        food.move()
    if food.ycor() < -360:
        food.hide()
        food.create_food()

    for part in paddle.all_parts:
        if part.distance(food) < 15:
            if food.shape() == "turtle" :
                food.hide()
                window.bgcolor("red")
                score.game_over()
                game_on= False
            else:
                score.increase(2)
                food.hide()
                food.create_food()



    time.sleep(0.003)
    window.update()
window.exitonclick()