from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, Massage


def start_game():
    global game_start
    game_start = True
    massage.clear()
    s_board.read_file()


def try_again():
    global game_start
    game_start = False


def game_done():
    global game_is_on
    game_is_on = False
    massage.press_massage()


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
s_board = ScoreBoard()
massage = Massage()

screen.listen()
screen.onkeypress(start_game)
screen.onkey(game_done, "Escape")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_start = False
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    if game_start:
        s_board.write_score()
        snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        s_board.increase_score()
        snake.extend()

    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 300:
        massage.end_massage()
        s_board.score = 0
        try_again()
        snake.remove_segments()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            massage.end_massage()
            s_board.score = 0
            try_again()
            snake.remove_segments()


screen.exitonclick()
