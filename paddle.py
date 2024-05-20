from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DIST = 30

class Paddle(Turtle):

    def __init__(self, cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.goto(cor)

    def up(self):
        self.setheading(UP)
        self.move()

    def down(self):
        self.setheading(DOWN)
        self.move()

    def move(self):
        self.forward(MOVE_DIST)
