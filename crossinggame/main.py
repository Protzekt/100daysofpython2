import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.up, "w")
screen.onkey(turtle.down,"Down")
screen.onkey(turtle.down,"s")

times_slept = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    times_slept += 1
    screen.update()
    if times_slept % 6 == 0:
        car_manager.car_maker()
        car_manager.move()
        times_slept = 0
    for car in car_manager.total_cars:
        if turtle.distance(car) < 22:
            game_is_on = False

    if turtle.finished():
        turtle.return_to_start()
        car_manager.speed_up_cars()

screen.exitonclick()