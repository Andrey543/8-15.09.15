import time
#import turtle
#turtle.shape('turtle')
#turtle.speed('slowest')
def nyg(n):
    n=int(n)
    import turtle
    turtle.shape('turtle')
    turtle.speed('fastest')
    turtle.left(180-(180*(n-2)/(2*n)))
    for i in range(n):
        turtle.forward(10*n)
        turtle.left(180-(180*(n-2)/n))
    turtle.right(180-(180*(n-2)/(2*n)))
    turtle.penup()
    turtle.forward(3.3*n)
    turtle.pendown()
for i in range(3,13):  
     nyg(i)    
time.sleep(2)
