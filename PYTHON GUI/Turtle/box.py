import turtle
turtle.Screen()
t=turtle.Turtle("circle")
t.pencolor("green")
t.fillcolor("green")
t.speed(10)
t.begin_fill()
t.pensize(5)
t.forward(200)
t.left(90)
t.forward(200)
t.goto(0,0)
t.end_fill()
t.fillcolor("yellow")
t.begin_fill()
t.forward(-200)
t.left(-90)
t.forward(-200)
t.goto(0,0)
t.end_fill()
turtle.done()
