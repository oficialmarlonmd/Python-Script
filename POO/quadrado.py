class Quadrado():
    def __init__(self,lado=0.0):
        self.lado = lado

    def calculo_area(self):
        return self.lado ** 2
    
    def calculo_perimetro(self):
        return 4 * self.lado
    
    def info(self):
        self.lado = float(input('Digite o número que equivale aos lados do quadrado:'))

    def prints(self):
        print(f'A área do quadrado é {self.calculo_area()}')
        print(f'O perímetro do quadrado é {self.calculo_perimetro()}')

quadrado = Quadrado()

quadrado.calculo_area()
quadrado.calculo_perimetro()
quadrado.info()
quadrado.prints()