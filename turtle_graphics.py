# see documentation on the google
import random

import heroes
print(heroes.gen())

from turtle import Turtle,Screen
# from turtle import *
turtle1= Turtle()

turtle1.color("blue")
turtle1.shape("turtle")
turtle1.speed("fast")



# turtle1.hideturtle()   ---------->  to hide the turtle

# (height,width,not necessary)
turtle1.shapesize(2,2,2)
# def square():
#     turtle1.forward(100)
#     turtle1.left(90)
# for i in range(4):
#     square()



import random
color=["red","blue","green","orange","pink","black","brown"]
def pentagon(sides):
    angle=360/sides
    for i in range(sides):
        turtle1.forward(100)
        turtle1.right(angle)

for no_of_side in range(3,11):
    pentagon(no_of_side)
    turtle1.color(random.choice(color))



# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         turtle1.color(c)
#         turtle1.forward(steps)
#         turtle1.right(30)



screen = Screen()
screen.exitonclick()
