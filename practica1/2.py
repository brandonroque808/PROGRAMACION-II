import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        return (-self.b + math.sqrt(self.getDiscriminante())) / (2*self.a)

    def getRaiz2(self):
        return (-self.b - math.sqrt(self.getDiscriminante())) / (2*self.a)

    def resolver(self):
        d = self.getDiscriminante()
        if d > 0:
            return f"La ecuacion tiene dos raices {self.getRaiz1()} y {self.getRaiz2()}"
        elif d == 0:
            return f"La ecuacion tiene una raiz {self.getRaiz1()}"
        else:
            return "La ecuacion no tiene raices reales"

#prueba
eq2 = EcuacionCuadratica(1.0, 3.0, 1.0)
print(eq2.resolver())
eq2b = EcuacionCuadratica(1.0, 2.0, 1.0)
print(eq2b.resolver())
eq2c = EcuacionCuadratica(1.0, 2.0, 3.0)
print(eq2c.resolver())
