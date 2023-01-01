import turtle
import time
from food import Food
from snake import Snake
from turtle import Turtle
from scoreboard import ScoreBoard
turtle.setup(width=600, height=600)
turtle.bgcolor('black')
turtle.title('My Snake Game')
tim = Turtle()
turtle.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
turtle.onkey(snake.Up, 'Up')
turtle.onkey(snake.Down, 'Down')
turtle.onkey(snake.Left, 'Left')
turtle.onkey(snake.Right, 'Right')
game_is_on = True
while game_is_on:
    turtle.update()
    time.sleep(0.05)
    turtle.listen()
    snake.move()

    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.gameover()

    # detect collision with tail
    # if head collides with any segment in snake
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            game_is_on = False
            scoreboard.gameover()
turtle.exitonclick()
print(f"your total score is {scoreboard.score}")

