import time
from turtle import Screen

from player import Player
from car_manager import CarManager

LEVEL = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Py Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_car()
    car_manager.move_cars()


screen.exitonclick()

