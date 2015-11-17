import time
import turtle
turtle.shape('classic')
turtle.speed(10)
def nyg(k,n):
    k=int(k)
    n=int(n)
    for i in range(120):
        turtle.forward(1+k/3)
        turtle.left(3*n)
turtle.right(90)
for i in range(1,10):
    nyg(i,1) 
    nyg(i,-1)       
time.sleep(2)
