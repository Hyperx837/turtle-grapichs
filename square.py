import turtle

pen = turtle.Turtle()
pen.color("red", "blue")

for _ in range(4):
    for _ in range(4):
        pen.forward(100)
        pen.left(90)
    pen.penup()
    pen.left(90)
    pen.forward(100)
    pen.pendown()

turtle.done()
