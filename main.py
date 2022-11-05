import turtle as t
from turtle import Screen
import random as rand

screen = Screen()

screen.title("Welcome to Delano's Hirst Emulation.")
screen.screensize(200, 200)
timmy_tortle = t.Turtle()
timmy_tortle.hideturtle()
timmy_tortle.speed(0)

# print(timmy_tortle.pos())
print(screen.window_height(), screen.window_width())



color_list = [ (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111)]
# TODO 1: The Hirst emulation should be a 10 by 10 grid of circles when completed

screen.colormode(255)

dots = 10
x_coord = -230
y_coord = -250
for _ in range(dots):
    timmy_tortle.penup()
    timmy_tortle.goto(x_coord, y_coord)
    for _ in range(dots):
        # TODO 2: Each of the dots should be 20 in size and spaced 50 apart from each other
        # setting the color of the dots
        color = rand.choice(color_list)
        timmy_tortle.pencolor(color)
        timmy_tortle.fillcolor(color)

        # making the dots
        timmy_tortle.dot(20, color)

        # spacing out the circles created
        if _ < dots-1:
            timmy_tortle.penup()
            timmy_tortle.forward(50)
    y_coord += 50

timmy_tortle.left(90)

timmy_tortle.pos()

screen.exitonclick()