import random
from turtle import Turtle, Screen

jim = Turtle()
jim.shape("classic")


def random_color():
    R = random.random()
    G = random.random()
    B = random.random()
    jim.pencolor(R, G, B)
    return random_color


jim.speed("fastest")


for _ in range(72):
    random_color()
    jim.circle(100)
    jim.left(5)


screen = Screen()
screen.exitonclick()