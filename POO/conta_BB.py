class Conta:
    def __init__(self, saldo=0.0, cheque_especial=1000):
        self.saldo = saldo
        self.cheque_especial = cheque_especial

    def saldos(self):
        consultar_saldo = input('Deseja consultar saldo "sim/não": ').lower()
        if consultar_saldo == 'sim':
            print(f'Seu saldo é R$ {self.saldo}')
        elif consultar_saldo == 'não':
            self.voltar_ao_menu()

    def depositar(self):
        valor_deposito = float(input('Qual o valor que deseja depositar: '))
        self.saldo += valor_deposito
        print('Seu saldo foi depositado com sucesso!')
        self.voltar_ao_menu()

    def sacar_dinheiro(self):
        print(f'Seu saldo é de R$ {self.saldo}')
        retirar = float(input('Quanto deseja sacar: '))
        if self.saldo >= retirar:
            self.saldo -= retirar
            print(f'Seu saldo atual é de R$ {self.saldo}')
        else:
            print('Saldo insuficiente.')
            usar_cheque = input(f'Seu saldo é de R$ {self.saldo}, deseja "1. Depositar" ou "2. Usar o Cheque Especial"  opção "1 ou 2": ')
            if usar_cheque == '1':
                self.depositar()
            elif usar_cheque == '2':
                self.usar_cheque_especial()
        self.voltar_ao_menu()

    def usar_cheque_especial(self):
        while True:
            if self.saldo == 0.0:
                cheque = input('Você não tem saldo, deseja usar o cheque especial "sim/não": ')
                if cheque == 'sim':
                    saque = float(input(f'Seu cheque especial é de R$ {self.cheque_especial}, quanto deseja sacar: '))
                    if self.cheque_especial >= saque:
                        juros = saque * (14/100)
                        self.cheque_especial -= (saque + juros)
                        print(f'Você acabou de sacar o valor de R$ {saque} e resta o valor de R$ {self.cheque_especial} no cheque especial!')
                    else:
                        print('Valor do saque excede o limite do cheque especial.')
                else:
                    print('Opção inválida!')
            resposta = input('Deseja fazer outro saque? Sim/Não ').lower()
            if resposta != 'sim':
                break
        self.voltar_ao_menu()

    def print_opcao(self):
        print('1. Consultar saldo')
        print('2. Depositar')
        print('3. Sacar')
        print('4. Cheque especial')

    def escolher_opcao(self):
        try:
            opcao_escolha = int(input('Escolha uma das opções numéricas acima: '))
            if opcao_escolha == 1:
                self.saldos()
            elif opcao_escolha == 2:
                self.depositar()
            elif opcao_escolha == 3:
                self.sacar_dinheiro()
            elif opcao_escolha == 4:
                self.cheque_especial()
            else:
                self.opcao_invalida()
        except ValueError:
            self.opcao_invalida()

    def opcao_invalida(self):
        print('ERRO! OPÇÃO INVÁLIDA!!!')

    def voltar_ao_menu(self):
        voltar = input('\n Pressione "s" no teclado para voltar ao menu inicial: ')
        if voltar.lower() == 's':
            self.print_opcao()
            self.escolher_opcao()
        else:
            print('Finalizando o programa...........................')

cliente_1 = Conta()
cliente_1.print_opcao()
cliente_1.escolher_opcao()