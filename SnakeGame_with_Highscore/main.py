import time
from turtle import Screen
from scoreboard import Scoreboard

from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python snake game")
screen.tracer(0)
score = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_block()
        scoreboard.score_up()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.new_score()
        snake.restart_game()

    # Detect collision ith body
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.new_score()
            snake.restart_game()

screen.exitonclick()
