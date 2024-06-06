def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida"

print('''Calculadora!
      Seja bem-vindo a nossa calculadora simples!''')

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

operadores = input('''Digite qual dos operadores deseja para realizar o cálculo, matemático,
                   soma, subtracao, multiplicacao, divisao: ''')

match operadores:
    case 'soma':
        resultado = soma(a, b)
    case 'subtracao':
        resultado = subtracao(a, b)
    case 'multiplicacao':
        resultado = multiplicacao(a, b)
    case 'divisao':
        resultado = divisao(a, b)
    case _:
        print('ATENÇÃO!!! Você escolheu um operador que não existe!!!')

print('Resultado: ', resultado)
