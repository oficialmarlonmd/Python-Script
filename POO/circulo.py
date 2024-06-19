class Circulo:
    def __init__(self, raio=0.0):
        self.raio = raio
        self.PI = 3.14

    def calcular_área(self):
        return self.PI * (self.raio**2)

    def calcular_perimetro(self):
        return 2 * self.PI * self.raio
    
    def info(self):
        self.raio = float(input('Digite o raio: '))
    
    def prints(self):
        print(f'A área é  {self.calcular_área()}')
        print(f'O perímetro {self.calcular_perimetro()}')


circulo = Circulo()

circulo.info()
circulo.calcular_área()
circulo.calcular_perimetro()
circulo.prints()