import turtle

deb = turtle.Turtle()
deb.penup()
deb.goto(-150, 10)
deb.pendown()
deb.speed(1000)
deb.getscreen().bgcolor("red")
deb.color("blue", "yellow")


def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size / 3)
            turtle.left(216)
        turtle.end_fill()


star(deb, 300)
turtle.done()
