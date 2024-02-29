from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard
import time
X_Y_DIMENSION = 600

screen = Screen()
screen.setup(width=X_Y_DIMENSION, height=X_Y_DIMENSION)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.turn_snake(screen)

    if snake.turtle.distance(food) < 15:
        food.refresh()
        score.updatescore()

    if snake.turtle.xcor() > 280 or snake.turtle.xcor() < -280 or snake.turtle.ycor() > 280 or snake.turtle.ycor() < -280:
        game_is_on = False
        score.end_game()


screen.exitonclick()
