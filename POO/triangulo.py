import math

class TrinaguloEquilatero():
    def __init__(self, lado=0.0):
        self.lado = lado

    def calcular_area(self):
        return (math.sqrt(3) / 4 * (self.lado**2))
    
    def calcular_perimetro(self):
        return 3 * self.lado
    
    def info(self):
        self.lado = float(input('Digite o número que equivale os lados do triângulo equilatero: '))
    
    def prints(self):
        print(f'A área do triangulo é {self.calcular_area()}')
        print(f'O perímetro do triângulo é {self.calcular_perimetro()}')
    
triangulo = TrinaguloEquilatero()
triangulo.calcular_area()
triangulo.calcular_perimetro()
triangulo.info()
triangulo.prints()