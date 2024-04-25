from turtle import Turtle
ALIGN = "center"
FONT = ("arial", 15, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
