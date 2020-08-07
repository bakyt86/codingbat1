from turtle import *

shape("turtle")

def up():
    setheading(90)
    forward(100)

def down():
    setheading(270)
    forward(100)

def left():
    setheading(180)
    forward(100)

def right():
    setheading(0)
    forward(100)

onkey(up, "Up")
onkey(down, "Down")
onkey(left, "Left")
onkey(right, "Right")


    
listen()
