import turtle
import math

pen = turtle.Turtle()
pen.speed(0)


def starfish(n=None):
    if n is not None and not n % 360:
        return

    if n is None:
        n = 0
    pen.forward(40)
    pen.left(math.sin(n) * math.cos(n) + n)
    starfish(n + 30)


starfish(179)
turtle.done()