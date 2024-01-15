
from turtle import Turtle

#CONSTANTS:
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 270)
        self.write_the_scoreboard()


    def write_the_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write_the_scoreboard()

    def game_over_display(self):
        self.goto(0, 0)
        self.write(f"GAME OVER DUDE/DUDETTE.", move=False, align=ALIGNMENT, font=FONT)





