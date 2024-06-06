# Atividade 04 Dic()
# 01
info = {'Nome': 'Miguel', 'Idade': 20,'Cidade': 'Sobradinho'}
        
        

print(f'''nome: {info['Nome']}
idade: { info['Idade']}
cidade: {info['Cidade']}''')

#02
info = {'Nome': 'Miguel', 'Idade': 20,'Cidade': 'Sobradinho'}

info['Idade'] = 46
print(info)

info['Profissao'] = 'Programador'
print(f'Profissão: {info['Profissao']}')

del info ['Cidade']
print(info)

# 03

quadrado = {}

for i in range(1, 6):
    quad = i**2
    quadrado[i] = quad                                   

# print(quadrado)

#04

chave = 1

if chave in quadrado:
    print(f'A chave {chave} existe no dicionário.')
else:
    print(f'Essa chave {chave} não existe nop dicionário.')

# 05

frase = "Estou programando em python."

frase = frase.lower()
palavras = frase.split()

frequencia = {}

for i in palavras:
    if i in frequencia:
        frequencia[i] += 1
    else:
        frequencia[i] = 1

print(f'A frenquêcia de palavras na frase é de {frequencia}')