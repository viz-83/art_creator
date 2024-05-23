import colorgram
import random
import turtle
from turtle import Screen
turtle.colormode(255)
tim=turtle.Turtle()
screen=Screen()

# rgb_colours=[]
# colors=colorgram.extract("image.jpg",30)
# for color in colors:
#     r=color.rgb.r
#     b= color.rgb.b
#     g= color.rgb.g
#     new_color=(r,g,b)
#     rgb_colours.append(new_color)
#
# print(rgb_colours)
colour_list=[(219, 154, 107), (132, 171, 196), (221, 73, 89), (215, 131, 150), (24, 119, 152), (241, 208, 98), (120, 176, 149), (38, 120, 85), (19, 165, 204), (223, 81, 74), (139, 87, 62), (130, 83, 102), (174, 184, 217), (18, 168, 124), (161, 209, 166), (3, 97, 116), (170, 154, 78), (236, 161, 175), (238, 165, 152), (53, 60, 93), (150, 207, 221), (36, 59, 79), (103, 127, 171), (30, 91, 62), (233, 203, 18), (71, 75, 41)]

tim.hideturtle()
tim.speed(100)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
no_of_dots=101

for dot_count in range(1,no_of_dots):
    tim.dot(20,random.choice(colour_list))
    tim.penup()
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
