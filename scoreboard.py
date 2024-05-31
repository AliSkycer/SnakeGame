from turtle import Turtle
ALIGN = "center"
FONT = ("arial", 15, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.read_file()
        self.score = 0
        self.write_score()

    def read_file(self):
        file = open("highscore.txt", "r")
        self.highscore = int(file.read())
        file.close()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highscore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1

        if self.score > self.highscore:
            f = open("highscore.txt", "w")
            f.write(str(self.score))

        self.write_score()


class Massage(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 70)
        self.start_massage()

    def start_massage(self):
        self.clear()
        self.write("Press any key to start game.", align=ALIGN, font=FONT)

    def end_massage(self):
        self.clear()
        self.write("Press any key to play again or press Esc to exit game.", align=ALIGN, font=FONT)

    def press_massage(self):
        self.clear()
        self.write("click on screen to exit game.", align=ALIGN, font=FONT)
