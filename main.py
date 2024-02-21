from turtle import Screen
from snake_class import Snake
import time
X_Y_DIMENSION = 600

screen = Screen()
screen.setup(width=X_Y_DIMENSION, height=X_Y_DIMENSION)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.turn_snake(screen)


screen.exitonclick()
