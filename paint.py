import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
t1 = Turtle()

color = [(238, 253, 242), (252, 241, 247), (75, 179, 221), (234, 212, 94), (239, 158, 74), (225, 242, 250), (43, 110, 171), (225, 126, 157), (132, 236, 91), (89, 198, 22), (159, 187, 13), (177, 77, 32), (245, 153, 177), (226, 80, 50), (108, 216, 81), (49, 134, 216), (114, 218, 233), (36, 173, 209), (208, 84, 110), (60, 132, 26), (28, 62, 111), (190, 42, 50), (239, 169, 155), (19, 52, 90), (63, 106, 4), (174, 26, 33), (45, 104, 5), (165, 29, 23), (154, 194, 235)]
t1.setheading(225)
t1.penup()
t1.speed("fastest")
t1.forward(300)
t1.setheading(0)

def line():
    t1.setheading(90)
    t1.forward(50)
    t1.setheading(180)
    t1.forward(500)
    t1.setheading(360)

def dot():
    for _ in range(10):
        t1.dot(20,random.choice(color))
        t1.forward(50)

for i in range(10):
    dot()
    line()

t1.hideturtle()
screen = Screen()
screen.exitonclick()
