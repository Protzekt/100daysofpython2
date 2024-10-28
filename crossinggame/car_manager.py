from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.total_cars = []
        self.MOVE_INCREMENT = 10

    def car_maker(self):
        new_car = Turtle("square")
        new_car.color(COLORS[random.randint(0, 5)])
        new_car.penup()
        new_car.goto(280,random.randint(-250, 250))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.speed("fast")
        self.total_cars.append(new_car)

    def move(self):
        for car in self.total_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.MOVE_INCREMENT)

    def speed_up_cars(self):
        self.MOVE_INCREMENT += 3

