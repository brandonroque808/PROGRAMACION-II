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

    def validaNumero(self, n):
        return 0 <= n <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        while True:
            intento = int(input("Adivina un numero entre 0 y 10: "))
            if not self.validaNumero(intento):
                print("Numero invalido")
                continue
            if intento == self.numeroAAdivinar:
                print("Acertaste")
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

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10 and n % 2 == 0:
            return True
        print("Numero invalido, debe ser par")
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10 and n % 2 == 1:
            return True
        print("Numero invalido, debe ser impar")
        return False

class Aplicacion:
    @staticmethod
    def main():
        juegos = [JuegoAdivinaNumero(3), JuegoAdivinaPar(3), JuegoAdivinaImpar(3)]
        for j in juegos:
            j.juega()

Aplicacion.main()
