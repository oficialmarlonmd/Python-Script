class Aluno():
    def _init_(self):
        self.nome = input('Digite seu nome: ')
        self.notas = []
        
    def adicionar_notas(self):
        for n in range(4):
            notas = float(input('Digite sua nota: '))
            self.notas.append(notas)

    def media_nota(self):
        media = sum(self.notas) / len(self.notas)
        print(f'A media do aluno é {media}')
      
aluno_1 = Aluno()
    
aluno_1.adicionar_notas()
aluno_1.media_nota()