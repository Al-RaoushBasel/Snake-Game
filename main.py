import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
# screen background color
screen.bgcolor("black")
screen.title("the snake game")

screen.tracer(0)

score_board = ScoreBoard()
snake = Snake()
food = Food()


# screen detects presses on the keyboard

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        score_board.increase_score()
        score_board.update_scoreboard()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -320 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()



screen.exitonclick()
