l = 3
ints = 1
 
def setup():
  fullScreen()
  
def draw():
    background(0, 0, 255)
    translate(width/2, height/2)
    stroke(255)
    turn_left(l, ints)
    turn_right(l, ints)

def mousePressed():
    global ints
    ints += 1
 
def turn_right(l, ints):
    if ints == 0:
        line(0, 0, 0, -l)
        translate(0, -l)
    else:
        turn_left(l, ints - 1)
        rotate(radians(90))
        turn_right(l, ints - 1)
 
def turn_left(l, ints):
    if ints == 0:
        line(0, 0, 0, -l)
        translate(0, -l)
    else:
        turn_left(l, ints - 1)
        rotate(radians(-90))
        turn_right(l, ints - 1)
