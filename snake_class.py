from turtle import Turtle
CO_ORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_turtles()
        self.turtle = self.turtles[0]

    def create_turtles(self):
        for i in CO_ORDINATES:
            turtle_name = f'turtle_{CO_ORDINATES[0][0] +1}'
            turtle_name = Turtle(shape='square')
            turtle_name.color('white')
            turtle_name.penup()
            turtle_name.goto(i)
            self.turtles.append(turtle_name)

    def move(self):
        for each_turtle in range((len(self.turtles)-1), 0, -1):
            new_x = self.turtles[each_turtle-1].xcor()
            new_y = self.turtles[each_turtle-1].ycor()
            self.turtles[each_turtle].goto(new_x, new_y)
        self.turtles[0].back(MOVE_DISTANCE)

    def turn_left(self):
        ...

    def turn_up(self):
        self.turtle.seth(90)

    def turn_right(self):
        ...

    def turn_down(self):
        self.turtle.seth(180)

    def turn_snake(self, screen):
        screen.onkey(key='Up', fun=self.turn_up)
        screen.onkey(key='Down', fun=self.turn_down)
        screen.onkey(key='Left', fun=self.turn_left)
        screen.onkey(key='Right', fun=self.turn_right)
