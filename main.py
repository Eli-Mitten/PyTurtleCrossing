import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Py Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(GAME_SPEED)
    screen.update()

    car_manager.create_new_car()
    car_manager.move_cars()

    for car in car_manager.garage:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 300:
        player.restart_position()
        scoreboard.level_up()
        GAME_SPEED *= 0.9


screen.exitonclick()

