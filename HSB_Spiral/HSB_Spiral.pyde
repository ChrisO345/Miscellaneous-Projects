
t = speed = 4e-5;
q = qq = rot = 0;
l = 0;
rads = [None, None, None];
quantity = 100

def setup():
    global l, quantity
    # size(600, 600);
    fullScreen()
    colorMode(HSB,1);
    l = 90;
    strokeWeight(1.5);
    for i in range(3, quantity):
        rads.append(l/(2*tan(PI/i))) 
    
def poly(N):
    for i in range(N):
        push();
        rotate(TWO_PI*i/N);
        line(-l/2, rads[N], l/2, rads[N]);
        pop();

def dott(N, q):
    global qq, rot, rads
    q = (q + 0.5/N)%1;
    qq = (q*N)%1;
    rot = int(q*N);
    push();
    rotate(TWO_PI*rot/N);
    noStroke();
    ellipse(lerp(l/2, -l/2, qq), rads[N], l*.1, l*.1);
    pop();


def draw():
    global t, quantity
    t = speed*millis() - .01;
    background(255, 0, 255);
    push();
    translate(width/2,height/2);
    for i in range(quantity-1, 2, -1):
        stroke(map(i,3,quantity,0,1),.7,.9);
        poly(i);
    for i in range(3, quantity):
        fill(0.1);
        dott(i,(quantity-i)*t);
    pop();
