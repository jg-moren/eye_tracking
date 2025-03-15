import math

class dot:

    def __init__(self, p):
        if( isinstance(p,tuple)):
            self.x = p[0]
            self.y = p[1]
        else:
            self.x = p.x
            self.y = p.y

#
#   [a,b] * [c,d] = [a*c+b*e, a*d+b*f]
#           [e,f]
#
    def rot(self, sin, cos):
        x = self.x*cos+self.y*(-sin)
        y = self.x*sin+self.y*cos
        self.x = x
        self.y = y

    def __mul__(self, p):
        r = dot((self.x,self.y))
        if( isinstance(p,dot)):
            r.x *= p.x
            r.y *= p.y
        elif( isinstance(p, tuple)):
            r.x *= p[0]
            r.y *= p[1]
        else:
            r.x *= p
            r.y *= p
        return r

    def __sub__(self, p):
        r = dot((self.x,self.y))
        if( isinstance(p,dot)):
            r.x -= p.x
            r.y -= p.y
        elif( isinstance(p, tuple)):
            r.x -= p[0]
            r.y -= p[1]
        else:
            r.x -= p
            r.y -= p
        return r
    
    def __add__(self, p):
        r = dot((self.x,self.y))
        if( isinstance(p,dot)):
            r.x += p.x
            r.y += p.y
        elif( isinstance(p, tuple)):
            r.x += p[0]
            r.y += p[1]
        else:
            r.x += p
            r.y += p
        return r

    def get(self):
        return (int(self.x), int(self.y))

def dist(a,b):
    return math.sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))

def normalize( a, b, x ):
    if a == b :
        return dot(a),dot(b),dot(x) 
    p1 = dot(a)
    p2 = dot(b)
    p3 = dot(x)

    co = abs(p1.x - p2.x)
    ca = abs(p1.y - p2.y)
    hi = dist(p1,p2)
    cos = (co)/(hi)
    sin = (ca)/(hi)

    print(cos)
    print(sin)

    d = p1-p2

    d.rot(-sin,-cos)

    p2 = p1+d

    d = p1-p3

    d.rot(-sin,-cos)

    p3 = p1+d

    print(f"{p2.x},{p2.y}")

    return p1,p2,p3


    
