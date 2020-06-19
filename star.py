import turtle

pen = turtle.Turtle()
pen.speed(100)


def stars(size):
    if size < 11:
        return
    for _ in range(5):
        pen.forward(size)
        stars(size / 2)
        pen.left(216)


stars(170)

turtle.done()

