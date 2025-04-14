
import turtle 
t=turtle.Turtle()
t.color("black")
t.speed(100)
t.pu()
t.goto(-200,400)
t.pendown()
t.begin_fill()
for r in range(7):
    t.penup()
    t.fd(30)
    t.pendown()
    for x in range(4):
        t.fd(30)
        t.lt(90)

t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.end_fill()

t.color("black","red")
t.begin_fill()
for r in range(7):
    t.color("black","red")
t.begin_fill()
for r in range(7):
    for x in range(4):
        t.fd(30)
        t.lt(90)
    t.pu()
    t.fd(30)
    t.pd()
t.end_fill()
t.begin_fill()
t.color("black")
t.lt(90)
t.fd(30)
for x in range(4):
        t.rt(90)
        t.fd(30)
t.end_fill()  
t.pu()
t.goto(70,370)
t.pd()
t.begin_fill()
t.lt(90)
t.fd(30)
t.rt(90)
for x in range(4):
        t.fd(30)
        t.rt(90)
t.end_fill()
t.rt(90)
t.fd(30)
t.color("black","red")
t.begin_fill()
for r in range(7):
    t.color("black","red")
t.begin_fill()
for r in range(9):
    for x in range(4):
        t.fd(30)
        t.lt(90)
    t.pu()
    t.fd(30)
    t.pd()
t.end_fill()
t.begin_fill()
t.color("black")
t.lt(90)
t.fd(30)
for x in range(4):
        t.rt(90)
        t.fd(30)
t.end_fill() 
t.pu()
t.goto(100,340)
t.pd()

t.begin_fill()
t.lt(90)
t.fd(30)
t.rt(90)
for x in range(4):
        t.fd(30)
        t.rt(90)
t.end_fill()
t.rt(90)
t.fd(30)
t.color("black","red")
t.begin_fill()
for r in range(11):
    for x in range(4):
        t.fd(30)
        t.lt(90)
    t.pu()
    t.fd(30)
    t.pd()
t.end_fill()
t.begin_fill()
t.color("black","black")
t.fd(30)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(30)
t.end_fill()








turtle.done()