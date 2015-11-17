import time
import turtle
turtle.shape('classic')
turtle.speed(10)
def nyg(n):
    n=int(n)
    for i in range(60):
        turtle.forward(n)
        turtle.right(3)
turtle.left(90)
for i in range(20):
    nyg(2)
    nyg(1)           
time.sleep(2)
