import turtle
pen=turtle.Turtle
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fill_color('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def txt():
    pen.up()
    pen.setpos(100,99)
    pen.down()
    pen.color("black")
    pen.write("sudeep",font="bold")


pen.txt()
turtle.ht()
turtle
turtle.exitonclick()
