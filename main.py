from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

screen = Screen()
screen.setup(width=800, height=800)
screen.listen()

pen = Turtle()
pen.speed("fastest")
pen.hideturtle()
pen.pensize(5)



for _ in range(100):
    diameter = 20
    for _ in range(28):
        
        bg_color = (randint(0,255), randint(0,255), randint(0,255))
        rgb = (randint(0,255), randint(0,255), randint(0,255))
        
        pen.penup()
        pen.goto(x=0, y=-diameter)
        screen.bgcolor(bg_color)
        pen.pendown()
        pen.pencolor(rgb)
        pen.circle(diameter)
        
        diameter += 20


screen.exitonclick()