from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Create turtle.
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move_up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    # When player reaches finish_line, reset its position.
    def reset_position(self):
        self.goto(STARTING_POSITION)

    # Check if turtle is at finish_line.
    def at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
