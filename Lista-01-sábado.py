#Questão 01
print('Olá, Mundo!')


#Questão 02
nome = input('Qual é o seu nome?\n')
print(f'Olá {nome}, é um prazer te conhecer!')

#Questão 03
nome_func = input('Digite nome do funcioário: \n')
salario_func = int(input('Digite o salário: \n'))

print(f'O funcionário {nome_func}, tem  um salário de R$ {salario_func}, em Junho!')

#Questão 04

valor_1 = int(input('Digite um valor: \n'))
valor_2 = int(input('Digite outro valor: \n'))

soma = valor_1 + valor_2

print(f'A soma ente {valor_1} e {valor_2} é igual a {soma}!')

#Questão 05

nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))

media = (nota_1 + nota_2) /2

print(f'A média entre {nota_1} e {nota_2} é igual a {media} !')

#Questão 06

numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor de {numero} é {antecessor}')
print(f'O sucessor de {numero} é {sucessor}')

#Questão 07

num_r = float(input('Digite um número real: '))

print(f'O dobro de {num_r} é', num_r * 2)
print(f'A terça parte de {num_r} é', num_r /3)

#Questão 08

distancia_m = float(input('Digite uma distância em metros: '))

dam = distancia_m / 10
hm = distancia_m / 100
km = distancia_m / 1000
dm = distancia_m * 10
cm = distancia_m * 100
mm = distancia_m * 1000

print(f'''A distância de {distancia_m}m corresponde a:
{km}km		{dm}dm
{hm}hm		{cm}cm
{dam}dam		{mm}mm''')

#Questão 09

valor_r = float(input('Digite quanto tens em R$: '))

dolar = valor_r * 0.20

print(f'Você tem R$ {valor_r} em sua carteira e pode comprar $ {dolar}')

#Questão 10
altura_p = float(input('Digite a altura da parede: '))

largura_p = float(input('Digite a largura da parede: '))

area = largura_p * altura_p

qtd_t = area / 2


print(f'A área a ser pintada é de : {area}m2  e serão gastos {qtd_t}L')

# #Questão 11

a = float(input('Digite o valor 01: '))
b = float(input('Digite o valor 02: '))
c = float(input('Digite o valor 03: '))

delta_f = (b**2 - 4 * a * c)

print(f'O valor de delta é: {delta_f}')

#Questão 12

preco_p = float(input('Digite o preço atual do produto: '))

desconto = preco_p * (5/100) 
peco_final = preco_p - desconto
print(f'O PREÇO PROMOCIONAL com 5% de desconto é de {peco_final}!')

# #Questão 13

salario = float(input('Digite seu salário: '))

aumento = salario * (15/100)
nv_salario = salario + aumento

print(f'Sou novo salário com 15% de aumento é de R${nv_salario}!')

# #Questão 14

km_percorrido = float(input('Digite a quantidade de Kms percorridos com o carro: '))
dias = int(input('Digite a quantidade e dias que o carro foi alugado: '))

total_percorrido = km_percorrido * (0.20)
total_dias = dias * 90

total_pagar = total_percorrido + total_dias

print(f'Total a pagar pelo aluguel do carra é de {total_pagar}')

# #Questão 15

dias_trab = int(input('Digite os dias trabalhados: '))

salario_m = (8 * 25) * dias_trab

print(f'Seu salário mensal é de R$ {salario_m}')

#Questão 16

nome_fumante = str(input('Digite o seu nome: '))
quantidade_cigarros = float(input('Digite a quantidade de cigarros que fuma por dia: '))
anos_fumante = float(input('Digite há quantos anos fuma: '))

qtd_dias = anos_fumante * 365
cigarros = quantidade_cigarros * qtd_dias

meses= cigarros * 10
dias_perdidos = meses/1440
dias_perdidos = int(dias_perdidos)

print(f'Sonhor(a) "{nome_fumante}" a quantidade de dias que perdeu foi de: {dias_perdidos}.')
