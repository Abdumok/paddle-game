from turtle import Screen
from paddle import Paddle

window= Screen()
window.bgcolor("black")
window.setup(width= 1000, height= 600)
window.title("Paddle Game v1.00")
window.tracer(0)

paddle= Paddle()




window.update()
window.exitonclick()