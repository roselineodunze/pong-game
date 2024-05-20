from turtle import Turtle

FONT = ("Courier", 70, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


