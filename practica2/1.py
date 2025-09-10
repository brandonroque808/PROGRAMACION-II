import math

class AlgebraVectorial:
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3

    def __add__(self,otro):
        return AlgebraVectorial(self.a1+otro.a1,self.a2+otro.a2,self.a3+otro.a3)

    def __sub__(self,otro):
        return AlgebraVectorial(self.a1-otro.a1,self.a2-otro.a2,self.a3-otro.a3)

    def __mul__(self,otro):
        return self.a1*otro.a1+self.a2*otro.a2+self.a3*otro.a3

    def __abs__(self):
        return math.sqrt(self.a1**2+self.a2**2+self.a3**2)

    def proyeccion(self,otro):
        esc=self*otro
        return AlgebraVectorial(otro.a1*(esc/(abs(otro)**2)),
                                otro.a2*(esc/(abs(otro)**2)),
                                otro.a3*(esc/(abs(otro)**2)))

    def componente(self,otro):
        return (self*otro)/abs(otro)

    def perpendicular(self,otro):
        return self*otro==0

    def paralela(self,otro):
        return self.a1*otro.a2==self.a2*otro.a1 and self.a1*otro.a3==self.a3*otro.a1

    def __str__(self):
        return f"({self.a1},{self.a2},{self.a3})"


a=AlgebraVectorial(1,2,3)
b=AlgebraVectorial(2,4,6)

print("a+b =",a+b)
print("a-b =",a-b)
print("a·b =",a*b)
print("|a| =",abs(a))
print("a perpendicular b:",a.perpendicular(b))
print("a paralela b:",a.paralela(b))
print("proyeccion de a sobre b:",a.proyeccion(b))
print("componente de a en b:",a.componente(b))
