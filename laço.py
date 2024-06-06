#Laço de repetição
#   Treinando 

for i in range(10, -1, -1):
    print(i)
print('Fim!!!')

num = int(input('Digite um número: '))
for i  in range(0, num+1):
    print(i)

i = int(input('Inicio dos números: '))
f = int(input('Digite o final da contagem: '))
p = int(input('Digite de quanto em quanto deseja chegar ao valor final: '))
for i in range(i, f+1, p):
    print(i)
print('FIM!!!')

soma = 0
for i in range(0, 4):
    num = int(input('Digite o valor: '))
    #somatório soma = soma + n ou
    soma += num
print(f'A soma dos valores foi {soma}!!!')