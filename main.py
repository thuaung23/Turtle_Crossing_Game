import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create the display.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

# Create keys to move the turtle up and down.
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Check if player collides with a car.
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Check if player makes to finish line.
    if player.at_finish_line():
        player.reset_position()
        score.add_level()


screen.exitonclick()
