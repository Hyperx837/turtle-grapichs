import turtle
import math

pen = turtle.Turtle()
pen.speed(100)


def random_pattern(n=None):
    if n is not None and not n % 360:
        return

    if n is None:
        n = 0
    pen.forward(10)
    pen.left(math.sin(n) * math.cos(n) + n)
    random_pattern(n + 100)


random_pattern(179)
turtle.done()
