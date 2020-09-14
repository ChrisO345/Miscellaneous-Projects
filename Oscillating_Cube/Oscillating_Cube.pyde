angle = 0
w = 5
ma = 0
maxD = 0

def setup():
    global ma, maxD
    size(400, 400, P3D)
    # fullScreen()
    ma = atan(cos(QUARTER_PI))
    maxD = dist(0, 0, 200, 200)

def draw():
    global angle, w, ma, maxD
    noStroke()
    lights()
    pointLight(50, 250, 50, 10, 30, 50)
    background(100)
    ortho(-400, 400, 400, -400, 0, 1000)
    rotateX(ma)
    rotateY(QUARTER_PI)
    translate(width/2 + 75, height/2 - 75)
    
    for z in range(0, height, w):
        for x in range(0, width, w):
            pushMatrix()
            d = dist(x, z, width / 2, height / 2)
            offset = map(d, 0, maxD, -PI, PI)
            a = angle + offset
            h = floor(map(sin(a), -1, 1, 100, 300))
            translate(x - width / 2, 0, z - height / 2)
            fill(255, 128, 0)
            box(w, h, w)
            #rect(x - width / 2 + w / 2, 0, w - 2, h);
            popMatrix()

    angle -= 0.1
