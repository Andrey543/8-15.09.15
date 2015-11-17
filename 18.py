import time
import turtle
turtle.shape('turtle')
turtle.speed('fastest')
def nyg():
    for i in range(120):
        turtle.forward(2)
        turtle.left(3)
for i in range(6):
    nyg()    
    turtle.left(60)
time.sleep(2)
