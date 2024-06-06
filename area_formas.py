#Atividade das formas geométricas

# 01 
while True:
    objetos = input('''Escolha um dos objetos a serguir
    Circurlo,
    Retângulo,
    Triângulo,
    Quadrado,
    R: ''')
    objetos = objetos.lower()

    if objetos == 'circulo':   
        raio = float(input('Informe o raio: '))
        area_circulo = 3.14*raio**2
        perimetro = 2*3.14*raio
        print(f'Área do circulo é {area_circulo}, o perímetro do circulo é {perimetro}.')
    elif objetos == 'retângulo':
        comprimento = float(input('Digite o comprimento:'))
        largura = float(input('Digite a largura do retângulo: '))
        area_retangulo = comprimento*largura
        perimetro_retangulo = 2*(comprimento+largura)
        print(f'Área do retângulo é {area_retangulo}, perímetro do retângulo é {perimetro_retangulo}.')
    elif objetos == 'triângulo':
        base = float(input('Digite a base do tranângulo: '))
        altura = float(input('Digite a altura do triângulo: '))
        area_triangulo = 0.5*base*altura
        print(f'Área do triângulo é {area_triangulo}.')
    elif objetos == 'quadrado':
        lado = float(input('Digite o lado do quadrado:'))
        area_quadrado = lado**2
        perimetro_quadrado = 4*lado
        print(f'Área do quadrado é {area_quadrado}, perímetro é {perimetro_quadrado}.')
    else:
        print('ERRO!Digite um do objetos existentes!!!')
    resposta = input('Você deseja consultar outro objeto? S/N: ').lower()
    if resposta != 's':
        break