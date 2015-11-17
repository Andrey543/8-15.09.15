import time
import turtle
turtle.shape('classic')
turtle.speed(10)
def nyg(n):
    n=int(n)
    for i in range(n):
        turtle.forward(100)
        turtle.left(180-180/n)
turtle.seth(180)
nyg(5)
turtle.penup()
turtle.backward(200)
turtle.pendown()
nyg(11)          
time.sleep(2)
