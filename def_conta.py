import os

saldo = 0.0

def consultar_saldo():
    global saldo
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    if saldo == 0.0:
        resposta = input('Seu saldo é de R$ 0.00, deseja depositar algum valor "sim/não": ').lower()
        if resposta == 'sim':
            depositar_valor()
    main()

def sacar_dinheiro():
    global saldo
    valor = float(input('Qual valor deseja sacar: R$ '))
    if saldo == 0.0:
        print('Você não possui saldo suficiente!')
    elif valor > saldo:
        print(f'O valor que deseja sacar é maior do que tem na sua conta que é de R$ {saldo:.2f}')
    else:
        saldo -= valor
        print('Operação realizada com sucesso!')
        voltar_ao_menu()
    main()
    

def depositar_valor():
    global saldo
    deposito = float(input('Qual valor deseja depositar: R$ '))
    saldo += deposito
    input('Deposito realizado com sucesso! Obrigado pela preferência......')
    voltar_ao_menu()
    main()


def prints():
    print('Bem-vindo a sua conta bancária!')
    print('1. Consultar saldo')
    print('2. Sacar')
    print('3. Depositar')
    

def escolher_opcao():

    try:
        opcao_escolha = int(input('Escolha uma das opções numéricas acima: '))
        if opcao_escolha == 1:
            consultar_saldo()
        elif opcao_escolha == 2:
            sacar_dinheiro()
        elif opcao_escolha == 3:
            depositar_valor()
        else:
            opcao_invalida()
    except ValueError:
            opcao_invalida()
            
def opcao_invalida():
    print('ERRO! OPÇÃO INVÁLIDA!!!')
    main()
    
def voltar_ao_menu():
    voltar = input('\n Pressione "s" e "Enter" no teclado para voltar ao menu inicial: ')
    if voltar.lower() == 's':
        prints()
        escolher_opcao()
    else:
        print('Finalizando o programa...........................')
    main()


def main():
    os.system('cls')
    prints()
    escolher_opcao()

main()