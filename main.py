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
window.textinput(title="How To Play", prompt="1- Square => 1 Point\n2- Circle => 3 Points"
                                            "\n3- Triangle => Reset the Score\n4- Turtle => Game Over")
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
        # collision with paddle and the shape was turtle:
        if part.distance(food) < 15:
            if food.shape() == "turtle" :
                food.hide()
                window.bgcolor("red")
                score.game_over()
                game_on= False
            # collision with paddle:
            else:
                # the shape is triangle: reset the score:
                if food.shape() == "triangle":
                    score.score =0
                # the shape is triangle: add 1 point:
                elif food.shape() == "square":
                    score.increase(1)
                # the shape is circle: add 3 point:
                elif food.shape() == "circle":
                    score.increase(3)
                food.hide()
                food.create_food()
                print(food.shape())



    time.sleep(0.003)
    window.update()
window.exitonclick()