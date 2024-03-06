from turtle import Turtle
from random import randint


class Bonus(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color('green')
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
