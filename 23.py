import time
import turtle
turtle.shape('classic')
turtle.speed(10)
def draw(l, n):
    n=int(n)
    l=int(l)
    if n==1:
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        turtle.right(120)
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
    else:
        draw(l/3,n-1)
        turtle.left(60)
        draw(l/3,n-1)
        turtle.right(120)
        draw(l/3,n-1)
        turtle.left(60)
        draw(l/3,n-1)
    
for i in range(3):
    draw(81,4)
    turtle.right(120)
time.sleep(2)
        
