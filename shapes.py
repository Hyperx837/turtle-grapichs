import turtle
import sys
import math

sys.setrecursionlimit(10000)

pen = turtle.Turtle()
pen.speed(100)
pen.penup()
pen.left(-90)
pen.forward(200)
pen.left(90)
pen.pendown()
# pen.goto(100, 700)


def shapes(n, times=0):
    if times == 5000:
        return
    pen.forward(math.sqrt(n * 2) * 5)
    pen.left(math.sin(n) ** 2 + n + math.cos(n) ** 2)
    shapes(n + 0.1, times + 1)


shapes(2)
