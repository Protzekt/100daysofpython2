from turtle import Turtle


def state_namer(xcor, ycor, state):
    staternamer = Turtle("square")
    staternamer.hideturtle()
    staternamer.shape("turtle")
    staternamer.penup()
    staternamer.color("Black")
    staternamer.goto(xcor, ycor)
    staternamer.write(state)
