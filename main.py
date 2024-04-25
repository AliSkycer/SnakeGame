from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
s_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        s_board.increase_score()
        snake.extend()

    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 300:
        game_is_on = False
        s_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            s_board.game_over()





screen.exitonclick()
