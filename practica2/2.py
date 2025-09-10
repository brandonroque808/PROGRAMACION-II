import math

class Vector:
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3

    def __add__(self,otro):
        return Vector(self.a1+otro.a1,self.a2+otro.a2,self.a3+otro.a3)

    def escalar(self,r):
        return Vector(r*self.a1,r*self.a2,r*self.a3)

    def __abs__(self):
        return math.sqrt(self.a1**2+self.a2**2+self.a3**2)

    def normal(self):
        m=abs(self)
        return Vector(self.a1/m,self.a2/m,self.a3/m)

    def __mul__(self,otro):
        return self.a1*otro.a1+self.a2*otro.a2+self.a3*otro.a3

    def __xor__(self,otro):
        return Vector(self.a2*otro.a3-self.a3*otro.a2,
                      self.a3*otro.a1-self.a1*otro.a3,
                      self.a1*otro.a2-self.a2*otro.a1)

    def __str__(self):
        return f"({self.a1},{self.a2},{self.a3})"


a=Vector(1,2,3)
b=Vector(4,5,6)

print("a+b =",a+b)
print("2a =",a.escalar(2))
print("|a| =",abs(a))
print("normal de a =",a.normal())
print("a·b =",a*b)
print("a×b =",a^b)
