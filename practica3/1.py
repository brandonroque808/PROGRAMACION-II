import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3

    def actualizaRecord(self):
        self.record += 1

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        while True:
            intento = int(input("Adivina un numero entre 0 y 10: "))
            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    print("No te quedan vidas")
                    break

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

Aplicacion.main()
