from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.writescore()
        self.hideturtle()

    def writescore(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT,
                   font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER !", align=ALIGNMENT,
                   font=FONT)

    def updatescore(self):
        self.score += 1
        self.clear()
        self.writescore()
