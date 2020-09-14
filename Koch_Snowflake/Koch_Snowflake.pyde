segments = []

def addAll(arr, segmentList):
    for s in arr:
        segmentList.append(s)
    return segmentList

def setup():
    global segments
    size(600,800)
    a = PVector(0, 100)
    b = PVector(600, 100)
    s1 = Segment(a, b)
    
    leng = PVector.dist(a, b)
    h = leng * sqrt(3) / 2
    c = PVector(300, 100+h)
    
    s2 = Segment(b, c)
    s3 = Segment(c, a)
    segments.append(s1)
    segments.append(s2)
    segments.append(s3)
    
def mousePressed():
    global segments
    nextGeneration = []
    for s in segments:
        children = s.generate()
        nextGeneration = addAll(children, nextGeneration)
    segments = nextGeneration

def draw():
    background(0)
    translate(0, 100)
    
    stroke(255)
    for s in segments:
        s.show()





class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def generate(self):
        a = self.a
        b = self.b
        children = [None, None, None, None]
        v = PVector.sub(b,a)
        v.div(3)
        
        b1 = PVector.add(a,v)
        children[0] = Segment(a, b1)
        
        a1 = PVector.sub(b,v)
        children[3] = Segment(a1, b)
        
        v.rotate(-PI/3)
        c = PVector.add(b1,v)
        children[1] = Segment(b1, c)
        
        children[2] = Segment(c, a1)
        return children
    
    def show(self):
        a = self.a
        b = self.b
        stroke(255)
        line(a.x, a.y, b.x, b.y)
        
        
