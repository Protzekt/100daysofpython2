import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.up, "w")
screen.onkey(turtle.down,"Down")
screen.onkey(turtle.down,"s")











game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
