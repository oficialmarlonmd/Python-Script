class Retangulo():
    def __init__(self, largura=0.0, altura=0.0):
        self.largura = largura
        self.altura = altura
    
    def calculo_area(self):
        return self.largura * self.altura
    
    def calculo_perimetro(self):
        return 2 * (self.largura +  self.altura)
    
    def info(self):
        self.largura = float(input('Digite a largura do retângulo: '))
        self.altura = float(input('Digite a altura do retângulo: '))
        if self.largura <= self.altura:
            print('A largura que digitou do retangulo é menor que a altura')
            self.info()

    def prints(self):
        print(f'A área do retângulo é {self.calculo_area()}')
        print(f'O perímetro do retângulo é {self.calculo_perimetro()}')

retangulo = Retangulo()

retangulo.calculo_area()
retangulo.calculo_perimetro()
retangulo.info()
retangulo.prints()