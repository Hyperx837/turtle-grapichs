import turtle
import math

pen = turtle.Turtle()
pen.speed(100)


def random_pattern(n):
    pen.forward(100)
    pen.left(math.sin(n) * math.cos(n) + n)
    random_pattern(n + 100)


turtle.done()
