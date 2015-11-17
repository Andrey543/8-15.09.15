import time
import turtle
turtle.shape('classic')
turtle.speed(10)
def draw(l, n):
    n=int(n)
    l=int(l)
    if n==1:
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(2*l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
    else:
        draw(l/4,n-1)
        turtle.left(90)
        draw(l/4,n-1)
        turtle.right(90)
        draw(l/4,n-1)
        turtle.right(90)
        draw(l/4,n-1)
        draw(l/4,n-1)
        turtle.left(90)
        draw(l/4,n-1)
        turtle.left(90)
        draw(l/4,n-1)
        turtle.right(90)
        draw(l/4,n-1)
turtle.penup()        
turtle.backward(400)
turtle.pendown()
for i in range(1):
    draw(1048576,10)
time.sleep(2)


        
