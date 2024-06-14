# Atividade 1 de Programação Orientada a Objeto

lista_heroi = ['Superman', 'SuperForça', 'Kriptonita']

lista_ponto_fraco = ['Kriptonita', 'Prata','Burrice', 'Pobreza']

class Heroi():
    def __init__(self, nome, poder, ponto_fraco):
        self.nome = nome
        self.poder = poder
        self.ponto_fraco = ponto_fraco
    
    def escolha_ponto_fraco(self):
        self.nome = print('O herói é o Superman ele tem Superforça!')
        print(lista_ponto_fraco)
        self.ponto_fraco = input('Escolha um ponto fraco que está acima: ')
        if self.ponto_fraco in lista_heroi:
            print('Herói derrotado!')
            print(lista_heroi)
        else:
            print('Seu heroi não foi derrotado!')
            print(lista_heroi)

heroi_1 = Heroi(lista_heroi[0], lista_heroi[1], lista_heroi[2])
heroi_1.escolha_ponto_fraco()

