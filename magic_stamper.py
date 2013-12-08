"""       Krishnan Presents.....

           magic_stamper.py

Very crisp scribbler for kids

- Use Arrow buttons for moving Up, Down, Right and Left
- The number buttons 1,2,3,4,5,6,7,8,9 will increase the pen size
- Keys qwbeg can be used to select fill color
- Backspace will undo the last operation
- x will undo the last stamp done
- Esc will clear the window
- s c r t keys will draw square, circle, rectangle and triangle after required input is given
- Use left mouse button to click and scribble on the window
- colour buttons are given to change the pen colour
- spacebar will stamp drawing
-  steps.
 -------------------------------------------
                Try to draw!
 -------------------------------------------
    1. Using Mouse you can scribble anything
	2. Select color for fill
	3. Select shape for drawing
 -------------------------------------------
"""
from turtle import *
import sys

sys.setrecursionlimit(20000)
MESS = Turtle(visible=False)
COLOR_DICT = {'q' : 'black', 'w' : 'white', 'b' : 'blue',
              'g' : 'green', 'e' : 'red'}
STAMP_LIST = []

class ColorButton(Turtle):
    def __init__(self, col, x, y):
        Turtle.__init__(self)
        self.pu(); self.goto(x, y)
        self.color(col)
        self.shape("circle")
        self.onclick(self.setpencolor)
        self.onclick(self.setfillcolor, 3)
    def setpencolor(self, x, y):
        qw = pencolor(self.pencolor())
        print qw
    def setfillcolor(self, x, y):
        sw = fillcolor(self.pencolor())
        print sw

def jump(x,y):
    if x > -350:
        pu(); goto(x,y); pd()

def fill_switch():
    while True:
        fillindicator.fillcolor("red")
        yield begin_fill()
        fillindicator.fillcolor("")
        yield end_fill()   

def toggle_fill(x, y):
    fs.next

def goUp(val=10):
    MESS.clear()
    xpos = xcor()
    ypos = ycor()
    if (ypos+val) < 300:
	    goto(xpos, ypos+val)
    else:
	    show_message("Reached the limit")

def goDown(val=10):
    MESS.clear()
    xpos = xcor()
    ypos = ycor()
    if (ypos-val) > -300:
	    goto(xpos, ypos-val)
    else:
	    show_message("Reached the limit")

def goRight(val=10):
    MESS.clear()
    xpos = xcor()
    ypos = ycor()
    if (xpos+val) < 400:
	    goto(xpos+val, ypos)
    else:
	    show_message("Reached the limit")
	
def goLeft(val=10):
    MESS.clear()
    xpos = xcor()
    ypos = ycor()
    if (xpos-val) > -400:
	    goto(xpos-val, ypos)
    else:
	    show_message("Reached the limit")
	
def commit_shape():
    stid = stamp()
    STAMP_LIST.append(stid)

def delete_stamp():
    try:
	    stid = STAMP_LIST.pop()
        clearstamp(stid)
    except IndexError:
	    print "No Stamps to delete"
	    pass

def show_message(text):
    MESS.clear()
    MESS.write(text, align="center", font=("Courier", 14, "bold"))

def draw_square():
    begin_fill()
    side = int(input("Enter the length of side"))
    goUp(side)
    goLeft(side)
    goDown(side)
    goRight(side)
    end_fill()
                     
def draw_circle():
    begin_fill()
    rad = int(input("Enter value of radius"))
    circle(rad)
    end_fill()
 
def draw_rectangle():
    begin_fill()
    len = int(input("Enter the length"))
    bth = int(input("Enter the breadth"))
    goUp(bth)
    goLeft(len)
    goDown(bth)
    goRight(len)
    end_fill()

def draw_triangle():
    begin_fill()
    val = int(input("Enter the length of side"))
    right(60)
    forward(val)
    right(120)
    forward(val)
    right(60)
    forward(val)
    end_fill()

def main():
    global fs, fillindicator
    setup(800, 600, -20, 20)
    reset()
    shape("circle")
    shapesize(0.5)
    speed(0)
    fs = fill_switch()
    
    ondrag(goto)
    onscreenclick(jump)
    onscreenclick(toggle_fill, 2)
    for c in "123456789":
        def setpensize(s=int(c)):
            pensize(s)
            shapesize(outline=s)
        onkey(setpensize, c)
    for color in "qwbge":
        def setcolor(var=color):
            fillcolor(COLOR_DICT[var])
        onkey(setcolor, color)
    onkey(commit_shape, "space")
    onkey(clear, "Escape")
    onkey(undo, "BackSpace")
    onkey(delete_stamp, "x")
    onkey(goUp, "Up")
    onkey(goDown, "Down")
    onkey(goRight, "Right")
    onkey(goLeft, "Left")
    onkey(draw_square, "s")
    onkey(draw_circle, "c")
    onkey(draw_rectangle, "r")
    onkey(draw_triangle, "t")
    tracer(False)
    ColorButton("yellow", -365, 90)
    ColorButton("orange", -365, 60)
    ColorButton("red", -365, 30)
    ColorButton("violet", -365, 0)
    ColorButton("blue", -365, -30)
    ColorButton("green", -365, -60)
    ColorButton("black", -365, -90)
    fillindicator = Turtle(shape="turtle")
    fillindicator.pu()
    fillindicator.goto(-365, -180)
    fillindicator.color("black", "")
    tracer(True)
    listen()
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
