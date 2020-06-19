import math
import turtle

pen = turtle.Turtle()
pen.speed(100)
pen.color("red", "yellow")
pen.begin_fill()


def flower(n=None):
    if n is not None and not n % 360:
        return

    if n is None:
        n = 0

    pen.forward(100)
    pen.left(200)
    flower(n + 179)


flower()

turtle.done()
