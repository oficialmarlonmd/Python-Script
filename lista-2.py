# #Atividade-02

# #Questão 1
# velocidade_c = float(input('Digite a velocidade do veiculo: '))

# limite_velocidade = 80 

# if velocidade_c > limite_velocidade:
    
#     km_acima = velocidade_c - limite_velocidade
#     multa = km_acima * 5
    
#     print(f'Você foi multado no valor de {multa}')
# else:
#     print('Você está no limite de velocidade!')

# #Questão 02   
# ano = int(input('Digite o ano de nacimento: '))

# idade = 2024 - ano

# if idade >= 18 :
#     print('Você pode votar!')
# elif idade <= 17 :
#     print('Você não pode votar pois é menor')
    
# #Questão 03
# aluno_1 = input('Digite seu nome: ')
# nota_a1 = float(input('Digite sua primeira nota:'))
# nota_2_a1 = float(input('Digite sua segunda nota:'))

# media_a1 = (nota_a1 + nota_2_a1) /2

# aluno_2 = input('Digite seu nome: ')
# nota_a2 = float(input('Digite sua primeira nota:'))
# nota_2_a2 = float(input('Digite sua segunda nota:'))

# media_a2 = (nota_a2 + nota_2_a2) /2

# print(f'A média do aluno {aluno_1} é de {media_a1}')
# print(f'A média do aluno {aluno_2} é de {media_a2}')

# if media_a1 > media_a2:
#     print(f'A média do aluno {aluno_1} é maior {aluno_2}')

# else:
#     print(f'A média do aluno {aluno_2} é maior do que a média do {aluno_1}')

# #Questão 04
#  num =  int(input('Digite um número: ')) 
#  resul = num % 2

# if resul == 0:
#      print(f'O número {num} é par!')
# else:
#      print(f'O número {num} é impar!')

# #Questão 05
#  ano_bi = int(input('Digite o ano que deseja saber se é bissexto: '))
 
#  bissexto = ano_bi % 4
 
#  if bissexto == 0:
#      print(f'O ano de {ano_bi} é bissexto!')
#  else:
#      print('O ano não é bissexto!')

# #Questão 06

#  ano = int(input('Digite o ano que naceu: '))
 
#  resultado = 2024 - ano
#  maior = resultado - 18
#  menor = 18 - resultado
 
#  if resultado >= 18:
#      print(f'Se passaram {maior} anos do alistamernto!')
#  elif resultado < 18:
#      print(f'Faltam {menor} anos para se alistar')

# #Questão 07
# nome = input('Digite seu nome:')
# sexo = input('Digite seu sexo (m OU f): ')
# valor_c = float(input('Digite o valor da compra: '))

# desconto_m = valor_c - (5/100)
# desconto_f = valor_c - (13/100)

# if sexo in 'm':
#     print(f'Sua compra Sr.{nome} com o desconto 5% ficou R$ {desconto_m}!')
# elif sexo in 'f':
#     print(f'''Sua compra Sra.{nome} com 13% de desconto ficou R$ {desconto_f}!
# Feliz Dia das Mulheres!''')
    
# #Questão 08

# distancia_p = float(input('Digite a distância que deseja percorrer em KMs: '))

# preco_1 = distancia_p * 0.50

# if distancia_p > 200:
#     viagens_l = distancia_p * 0.45
#     print(f'O valor da corrida da distância de {distancia_p}km é de R$ {viagens_l}')
# else:
#     print(f'O valor da corrida da distância de {distancia_p}km é de R$ {preco_1}')

# #Questão 09
# def forma_triangulo(primeiro, segundo, terceiro):

#     if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
#         return True
#     else:
#          return False

# # Solicita os comprimentos dos segmentos de reta ao usuário
# primeiro = float(input("Informe o comprimento do primeiro segmento: "))
# segundo = float(input("Informe o comprimento do segundo segmento: "))
# terceiro = float(input("Informe o comprimento do terceiro segmento: "))

# #Verifica se é possível formar um triângulo
# if forma_triangulo(primeiro, segundo, terceiro):
#     print("É possível formar um triângulo com esses segmentos de reta.")
# else:
#     print("Não é possível formar um triângulo com esses segmentos de reta.")
    
# #Questão 10

# num_1 = int(input('Digite um número inteiro:'))
# num_2 = int(input('Digite outro número inteiro:'))

# if num_1 > num_2:
#     print('O primeiro valor é maior!')
# elif num_2 > num_1:
#     print('O segundo valor é maior')
# elif num_1 == num_2:
#         print('Não existe valor maior, os dois são iguais!')

# #Questão 11
        
# nome = input('Digite seu primeiro nome: ')
# nota_1 = float(input('Digite sua primeira nota: '))
# nota_2 = float(input('Digite sua segunda nota: '))

# media = (nota_1 + nota_2) /2

# if media <= 4.9:
#     print(f'''Aluno {nome} REPROVADO!
# Sua média está abaixo de 4.9, sua nota foi de {media}!!!''')
# elif 5 <= media <= 6.9:
#     print(f'''Aluno {nome} está de 	RECUPERAÇÃO!
# Nota: {media}''')
# elif media >= 7:
#     print(f'''Aluno {nome} está Aprovado!
# Nota: {media}''')

# #Questão 12

# largura = float(input('Digite a largura do terreno: '))
# comprimento = float(input('Digite o comprimento do terreno: '))

# area = largura * comprimento

# if area<= 100 :
#     print('TERRENO POPULAR!')
# elif 100 <= area and area <= 500:
#     print('TERRENO MASTER!')
# elif area >= 500:
#     print('TERRENO VIP!')

# #Questão 13

# 	nome = input('Digite seu nome: ')
# 	salario = float(input('Digite seu sálario R$:'))
# 	anos = int(input('Há quantos anos trabalha na empresa: '))

# salario_1 = salario * (3/100)
# salario_2 = salario * (12.5/100)
# salario_3 = salario * (20/100)

# if anos <= 3:
#     print(f'Sr.{nome} teve aumento de 3% R${salario_1}!')
# elif 3 <= anos and anos <= 10:
#     print(f'Sr.{nome} teve aumento de 12.5% R${salario_2}!')
# elif anos >= 10 :
#     print(f'Sr.{nome} teve aumento 20% R${salario_3}!')

# #Questão 14

# # Solicita os comprimentos dos segmentos de reta ao usuário

# 	primeiro = float(input("Informe o comprimento do primeiro segmento: "))
# 	segundo = float(input("Informe o comprimento do segundo segmento: "))
# 	terceiro = float(input("Informe o comprimento do terceiro segmento: "))

# #Virificar se é equilátero, isósceles e escaleno
# if primeiro == segundo and segundo == terceiro and terceiro == primeiro :
#     print('Equilátero!')
# elif primeiro == segundo != terceiro or segundo == terceiro != primeiro or terceiro == primeiro != segundo:
#     print('Isósceles!')
# elif primeiro != segundo != terceiro:
#     print('Escaleno')

# #Questão 15

# p_1 = input('Pessoa 1 para jogar JoKenPo escolha (Pedra-Papel-Tesoura): ')
# p_2 = input('Pessoa 2 para jogar JoKenPo escolha (Pedra-Papel-Tesoura): ')

# if  p_1 == 'pedra' and p_2 == 'tesoura' or p_1 == 'tesoura' and p_2 == 'papel' or p_1 == 'papel' and p_2 == 'pedra':
#     print('Pessoa 1 Você ganhou!')
# elif p_2 == 'pedra' and p_1 == 'tesoura' or p_2 == 'tesoura' and p_1 == 'papel' or p_2 == 'papel' and p_1 == 'pedra':
#     print('Pessoa 2 Você ganhou!')
# else:
#     print('Não existe essa forma de jogar!')

# #Questão 16
# from random import randint

# jogador = int(input('Digite o número de 1 a 5 que deseja adivinhar: '))

# a = randint(1,5)
# print(a)

# if jogador == a :
#     print('Você acertou!')
# else:
#     print('Tente novamente!')

# #Questão 17
# valor_c = float(input('Digite o valor da casa de deseja comprar: '))
# salario = float(input('Digite seu salário: '))
# anos =  int(input('Em quantos anos deseja pagar: '))

# meses = anos * 12
# prestacao = valor_c / meses
# porcento = salario * (30/100)

# if prestacao > porcento:
#     print('Não há possibilidade de emprestimos')
# elif prestacao <= porcento :
#     print(f'O valor da R$ {prestacao} da sua casa!')

# #Questão 18
# altura = float(input('Digite sua altura: '))
# peso = float(input('Digite seu peso: '))

# imc = peso/altura**2

# if imc < 18.5:
#     print('Abaixo do peso!')
# elif 18.5 < imc <= 25:
#     print('Peso ideal!')
# elif 25 < imc <= 30:
#     print('Sobrepeso!')
# elif 30 < imc <= 40:
#     print('Obesidade!')
# elif imc >= 40:
#     print('Obesidade mórbida!')

# #Questão 19

# while True:
#     carro = int(input('''DIGITE "1" PARA CARRO POPULAR
#     DIGITE "2" PARA CARRO DE LUXO: '''))
#     dias = int(input('Digite quantos dias você alugou o carro: '))
#     perc = float(input('Digite quantos Km foram percorridos: '))
#     if carro == 1:
#         days = dias * 90
#         if perc <= 100:
#             km = perc * 0.20
#         elif perc > 100:
#             km = perc * 0.10
#             print ('O valor total a pagar: R$', days + km)
#     if carro == 2:
#         days = dias * 150
#         if perc <= 200:
#             km = perc * 0.30
#         elif perc > 200:
#             km = perc * 0.25
#         print ('O valor do seu camaro é de: R$', days + km)
#     else:
#         print ('ESSE VALOR NÃO EXISTE!!!')
#     resposta = input('Deseja fazer outro cálculo? S/N ').lower()
#     if resposta !='s':
#         break

# #Questão 20

# while True:
# 	horas = float(input('Digite quantas horas de atividades físicas foram praticadas no mês: '))
#     if horas <= 10:
#         pontos = horas * 2
#         total = pontos * 0.05
#         print (f'Você praticou {horas} horas de exercícios, e faturou {pontos} pts. Sua recompensa é de: R${total}')
#     elif 10 < horas < 20:
#         pontos = horas * 5
#         total = pontos * 0.05
#         print (f'Você praticou {horas} horas de exercícios, e faturou {pontos} pts. Sua recompensa é de: R${total}')
#     else:
#         pontos = horas * 10
#         total = pontos * 0.05
#         print (f'Você praticou {horas} horas de exercícios, e faturou {pontos} pts. Sua recompensa é de: R${total}')
#     resposta = input ('Deseja fazer outro cálculo? S/N ').lower()
#     if resposta !='s':
#         break

# #Questão 21
# while True:
#     salario = float(input('Digite seu salário atual: '))
#     sexo = input('''Digite uma letra que corresponde ao seu sexo:
#                 M - MASCULINO
#                 F - FEMININO ''')
#     temp = int(input('Digite há quantos anos trabalha na empresa: '))

#     if sexo == 'F':  
#         if temp < 15:
#             aumento = salario * 0.05
#         elif 15 <= temp < 20:
#             aumento = salario * 0.12
#         else:
#             aumento = salario * 0.23
#     elif sexo == 'M':  
#         if temp < 20:
#             aumento = salario * 0.03
#         elif 20 <= temp < 30:
#             aumento = salario * 0.13
#         else:
#             aumento = salario * 0.25
    

#     novo_salario = salario + aumento
#     print(f'O aumento do seu salário foi de: R${aumento:.2f}, totalizando: R${novo_salario:.2f}')
    
#     resposta = input('Você deseja consultar outro aumento de salário? S/N: ').lower()
#     if resposta != 's':
#         break