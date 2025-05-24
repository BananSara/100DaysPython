from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='make your bet' , prompt='which turtle will win the race? Enter a color: ')

colors = ['red','orange','blue','green','purple','yellow']

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230 , y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'you have won! the {winning_color} turtle is the winner!')
            else:
                print(f'you have lost! the {winning_color} turtle is the winner!')

                print()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()


# practice event listeners
# def move_forwards():
#     new_turtle.forward(10)

# def move_backwards():
#     new_turtle.backward(10)

# def turn_left():
#     new_heading = new_turtle.heading() + 10
#     new_turtle.setheading(new_heading)

# def turn_right():
#     new_heading = new_turtle.heading() - 10
#     new_turtle.setheading(new_heading)

# def clear():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()

# screen.listen()
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='d', fun=turn_right)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='c', fun=clear)
