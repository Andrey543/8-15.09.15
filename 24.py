import time
import turtle
turtle.shape('classic')
turtle.speed(10)
def draw(l, n):
    n=int(n)
    l=int(l)
    if n==1:
        turtle.left(45)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(45)
    else:
        turtle.left(45)
        draw(l/2,n-1)
        turtle.right(90)
        draw(l/2,n-1)
        turtle.left(45)
        
    
for i in range(1):
    draw(1048576,20)
time.sleep(2)


        
