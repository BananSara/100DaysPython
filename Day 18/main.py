import turtle
from turtle import Turtle, Screen, colormode
import random
import colorgram

tim = Turtle()
tim.shape('turtle')
tim.color('green')


# draw a square
# for _ in range(4):
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

# Line:
# for i in range(0,15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors


# colours = ['black', 'orange', 'green', 'pink', 'purple', 'yellow', 'blue', 'red', 'LightSeaGreen','brown']
# directions = [0, 90, 180, 270]  # east,north,west,south
tim.speed('fastest')

# shapes:
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(180)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(colors())
#     draw_shape(shape_side_n)


# random walk:
# for _ in range(200):
# tim.color(random_color())
# tim.pensize(10)
# tim.forward(30)
# tim.setheading(random.choice(directions))

# spirograph:
# def spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random.choice(colours))
#         tim.circle(100)
#         current_heading = tim.heading()
#         tim.setheading(current_heading + 10)

# spirograph(5)

# spot painting:
colors = colorgram.extract('image.jpg', 15)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b= color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    
print(rgb_colors)

color_list = [(235, 234, 232), (240, 229, 235), (229, 238, 233), (225, 233, 238), (235, 37, 113), (143, 26, 67), (237, 72, 37), (220, 164, 55), (15, 140, 88), (174, 162, 50), (33, 122, 186), (52, 189, 227), (173, 44, 94), (242, 219, 57), (80, 24, 74)]
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(255)  # between 270 and 180
tim.forward(300)
tim.setheading(0)

num_of_dots = 100
for dot_count in range (1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
