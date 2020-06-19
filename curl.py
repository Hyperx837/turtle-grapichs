import turtle

pen = turtle.Turtle()
pen.speed(100)

pen.penup()
pen.left(-90)
pen.forward(250)
pen.left(90)
pen.pendown()

for i in range(600):
    pen.forward(20)
    pen.left(17 + i)

turtle.done()
