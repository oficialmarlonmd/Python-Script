class Conta:
    def __init__(self, saldo=0.0):
        self.saldo = saldo

    def consultar_saldo(self):
        self.saldo
        print(f'Seu saldo atual é de R$ {self.saldo}')
        if self.saldo == 0.0:
            resposta = input('Seu saldo é de R$ 0.00, deseja depositar algum valor "sim/não": ').lower()
            if resposta == 'sim':
                self.depositar_valor()

    def sacar_dinheiro(self):
        self.saldo
        valor = float(input('Qual valor deseja sacar: R$ '))
        if self.saldo == 0.0:
            print('Você não possui saldo suficiente!')
        elif valor > self.saldo:
            print(f'O valor que deseja sacar é maior do que tem na sua conta que é de R$ {self.saldo}')
        else:
            self.saldo -= valor
            print('Operação realizada com sucesso!')
        self.voltar_ao_menu()

    def depositar_valor(self):
        self.saldo
        deposito = float(input('Qual valor deseja depositar: R$ '))
        self.saldo += deposito
        print('Deposito realizado com sucesso! Obrigado pela preferência......')

        

    def prints(self):
        print('Bem-vindo a sua conta bancária!')
        print('1. Consultar saldo')
        print('2. Sacar')
        print('3. Depositar')
    

    def escolher_opcao(self):

        try:
            opcao_escolha = int(input('Escolha uma das opções numéricas acima: '))
            if opcao_escolha == 1:
                self.consultar_saldo()
            elif opcao_escolha == 2:
                self.sacar_dinheiro()
            elif opcao_escolha == 3:
                self.depositar_valor()
            else:
                self.opcao_invalida()
        except ValueError:
               self.opcao_invalida()
            
    def opcao_invalida(self):
        print('ERRO! OPÇÃO INVÁLIDA!!!')

    
    def voltar_ao_menu(self):
        voltar = input('\n Pressione "s" e "Enter" no teclado para voltar ao menu inicial: ')
        if voltar.lower() == 's':
            self.prints()
            self.escolher_opcao()
        else:
            print('Finalizando o programa...........................')

cliente_1 = Conta()

cliente_1.prints()
cliente_1.escolher_opcao()


