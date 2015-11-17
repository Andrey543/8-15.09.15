import turtle
import time
turtle.shape('classic')
turtle.speed('fastest')
k=20
for i in range(10):  
    for j in range(4): 
        turtle.forward(k)
        turtle.left(90)
    k+=20
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
time.sleep(1)
