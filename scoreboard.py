from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        # Show level at left upper corner.
        self.goto(-270, 260)
        self.update_scoreboard()

    # If player reaches finish_line, add 1 to current level.
    def add_level(self):
        self.level += 1
        self.update_scoreboard()

    # Display current level.
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # If player collides with any of the cars, display "Game Over" at the center.
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
