# snake game
from turtle import Screen
import time
from snake import Snake

# create screen:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  #animation off(for moving snake)

snake = Snake()

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

screen.exitonclick()