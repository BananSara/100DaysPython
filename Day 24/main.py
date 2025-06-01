# snake game
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# create screen:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  #animation off(for moving snake)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() 
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# move the snake:
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #delay for the argument
    snake.move()
    
    # detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # detect collision with tail:
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()