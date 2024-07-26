import random
from turtle import Turtle

X_STARTING = 320
DISTANCE_MOVE = 5


class CarManager:
    def __init__(self):
        self.garage = []

    def create_new_car(self, ):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(self.random_color())
            starting_y = random.randint(-250, 250)
            car.goto(X_STARTING, starting_y)
            self.garage.append(car)

    def move_cars(self):
        for car in self.garage:
            car.backward(DISTANCE_MOVE)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'#{r:02x}{g:02x}{b:02x}'
