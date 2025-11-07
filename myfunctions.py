import turtle
bob=turtle.Turtle()
turtle.tracer(False)
turtle.colormode(255)
turtle.bgcolor("grey")

def polygon(side,size,c):
    bob.color(c)
    bob.begin_fill()
    angle=360/side
    for times in range(side):
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()

def squarepattern():
    for times in range(255):
        c=(142, 141, 140)
        polygon(4,256-times,c)
        bob.left(100)
        c=(255,times,0)
        polygon(4,256-times,c)

def nonagonpattern():
    for times in range(255):
        c=(0+times,0+times,0+times)
        polygon(9,256-times,c)
        bob.right(100)
        c=(255,36,0)
        polygon(9,256-times,c)


def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    
def user():
    jump(0,380)
    bob.color("red")  
    style = ("Arial", 10, "bold")  
    bob.write("By Andrew Chen", font=style, align="center")

