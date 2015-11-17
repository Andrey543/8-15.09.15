import turtle
import time
turtle.shape('turtle')
turtle.speed('normal')
k=10
for i in range(40):   
    turtle.forward(k)
    turtle.left(90)
    k+=10
time.sleep(2)
