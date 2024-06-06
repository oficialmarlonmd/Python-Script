# Lista exercios 

# Questão 01 

lista_numero = [0, 1, 2, 3, 4, 5]
print(lista_numero)

# Questão 02

numero = int(input('Digite um valor até 100: '))

for i in range(1, numero +1):
   print(i)

# Questão 03 

numero = [30]

for valores in range(30, 0, -1 ):
    if valores % 4 == 0:
        print(f'[{valores}]', end=' ')
    else:
        print(valores, end=' ')

# Questão 04

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o último valor: '))
valor_3 = int(input('Digite o incremento: '))

for i in range(valor_1, valor_2+1, valor_3):
    print(i, end=' ')

# Questão 05

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o último valor: '))
valor_3 = int(input('Digite o incremento: '))

if valor_1 < valor_2 :
    for i in range(valor_1, valor_2+1, valor_3):
        print(i, end=' ')
else:
    for i in range(valor_2, valor_1+1, (valor_3)):
        print(i, end=' ')
    # for i in range(valor_1, valor_2+1, valor_3):
    #     print(i, end=' ')
        
# Questão 06

num = str(input('Digite 6 números inteiros separados: '))
lista = num.split()

lista_impar = []
lista_par = []

if len(lista) != 6:
    print('Erro! Digite os 6 números inteiros corretamente!!!')
else:
    for i in lista:
        i = int (i)
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
print(f'Lista de números pares ({lista_par})')
print(f'Lista de números impares ({lista_impar})')

# Questão 07
from random import randint

numeros_sorteados = []

for i in range(20):
    numeros = randint(0,10)
    numeros_sorteados.append(numeros)
print(f'Os números sorteados foram {numeros_sorteados}')

acima_de_5 = 0

for numero in numeros_sorteados:
    if numero > 5:
        acima_de_5 = acima_de_5 + 1

divisiveis_por_3 = 0 

for numero in numeros_sorteados:
    if numero % 3 == 0:
        divisiveis_por_3 = divisiveis_por_3 + 1

print("Quantidade de números acima de 5:", acima_de_5)
print("Quantidade de números divisíveis por 3:", divisiveis_por_3)

# Questão 08

precos = input('Digite o preço de 8 produtos separados por ",": ')
lista = precos.split(',')

maior_preco = float(lista[0])
menor_preco  = float(lista[0])

if len(lista) != 8:
    print('Erro! São 8 valores a serem digitados!!!')
else:
    for i in lista:
        i = float(i)
        
        if i > maior_preco:
            maior_preco += i
            
        elif i < menor_preco:
            menor_preco += i
            
print('Maior valor:R$ ',maior_preco)
print('Menor valor:R$ ',menor_preco)

# Questão 09

idades = []
maior_idade = 0
mais_de_18 = 0
menos_de_5 = 0

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)
    
    if idade > 18:
        mais_de_18 += 1
    if idade < 5:
        menos_de_5 += 1
    if idade > maior_idade:
        maior_idade = idade

media_idades = sum(idades) / len(idades)

print(f"A média de idade do grupo é: {media_idades:.2f} anos")
print(f"Quantidade de pessoas com mais de 18 anos: {mais_de_18}")
print(f"Quantidade de pessoas com menos de 5 anos: {menos_de_5}")
print(f"A maior idade lida foi: {maior_idade} anos")

# Questão 10

idades = []
homens = 0
mulheres = 0
idade_homem_total = 0
mulheres_mais_20 = 0

for i in range(5):
    print(f"Entrada de dados para a pessoa {i+1}:")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    
    idades.append(idade)
    
    if sexo == 'M':
        homens += 1
        idade_homem_total += idade
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulheres_mais_20 += 1


media_idade_grupo = sum(idades) / len(idades)
media_idade_homem = idade_homem_total / homens if homens > 0 else 0

print(f"Quantidade de homens cadastrados: {homens}")
print(f"Quantidade de mulheres cadastradas: {mulheres}")
print(f"A média de idade do grupo é: {media_idade_grupo:.2f} anos")
print(f"A média de idade dos homens é: {media_idade_homem:.2f} anos")
print(f"Quantidade de mulheres com mais de 20 anos: {mulheres_mais_20}")

# Questão 11


alturas = []
peso_mais_90 = 0
peso_menos_50_altura_menos_160 = 0
altura_mais_190_peso_mais_100 = 0


for i in range(7):
    print(f"Entrada de dados para a pessoa {i+1}:")
    peso = float(input("Peso (em Kg): "))
    altura = float(input("Altura (em metros): "))
    
    alturas.append(altura)
    
    if peso > 90:
        peso_mais_90 += 1
    if peso < 50 and altura < 1.60:
        peso_menos_50_altura_menos_160 += 1
    if altura > 1.90 and peso > 100:
        altura_mais_190_peso_mais_100 += 1


media_altura = sum(alturas) / len(alturas)


print(f"A média de altura do grupo é: {media_altura:.2f} m")
print(f"Quantidade de pessoas que pesam mais de 90Kg: {peso_mais_90}")
print(f"Quantidade de pessoas que pesam menos de 50Kg e medem menos de 1.60m: {peso_menos_50_altura_menos_160}")
print(f"Quantidade de pessoas que medem mais de 1.90m e pesam mais de 100Kg: {altura_mais_190_peso_mais_100}")

# Questão 12

import random

# O computador irá sortiar um número entre 1 e 10
numero_sorteado = random.randint(1, 10)
tentativas = 4

print("O computador sorteou um número entre 1 e 10.")
print(f"Você tem {tentativas} tentativas para acertar.")

# O jogador terá 4 tentativas para adivinhar o número
for tentativa in range(tentativas):
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou o número em {tentativa + 1} tentativas.")
        break
    else:
        print("Número incorreto. Tente novamente.")
        
    if tentativa == tentativas - 1:
        print(f"Suas tentativas acabaram. O número era {numero_sorteado}.")