import math

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos)/len(self.datos)

    def desviacion(self):
        p = self.promedio()
        return math.sqrt(sum((x - p)**2 for x in self.datos)/(len(self.datos)-1))

    def resolver(self):
        return f"El promedio es {self.promedio()}\nLa desviacion estandar es {self.desviacion()}"

#prueba
datos = [1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]
est = Estadistica(datos)
print(est.resolver())
