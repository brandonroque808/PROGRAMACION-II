class EcuacionLineal2x2:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tieneSolucion(self):
        return self.a * self.d - self.b * self.c != 0

    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)

    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)

    def resolver(self):
        if self.tieneSolucion():
            return f"x = {self.getX()}, y = {self.getY()}"
        else:
            return "La ecuacion no tiene solucion"

#prueba
eq1 = EcuacionLineal2x2(9.0, 4.0, 3.0, -5.0, -6.0, -21.0)
print(eq1.resolver())
eq1b = EcuacionLineal2x2(1.0, 2.0, 2.0, 4.0, 0.0, 5.0)
print(eq1b.resolver())
