import turtle
import time
turtle.shape('turtle')
turtle.speed('fastest')
k=1
for i in range(720):   
    turtle.forward(k)
    turtle.left(5)
    k+=0.005
time.sleep(2)
