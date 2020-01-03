import turtle
deb = turtle.Turtle()
deb.speed(10)
deb.getscreen().bgcolor("black")
deb.color("red","yellow")
deb.begin_fill()
for i in range(50):
    deb.forward(300)
    deb.left(170)
deb.end_fill()
turtle.done()
