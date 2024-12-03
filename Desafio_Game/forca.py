import random
from os import system, name

def limpa_tela():
    #Windows
    if name == 'nt':
        _ = system('cls')

    #Mac ou Linux
    else:
        _ = system('clear')


def game():
    limpa_tela()

    print('\nBem-Vindo ao Jogo da Forca!')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['manga', 'abacate', 'abacaxi', 'morango', 'laranja', 'uva', 'melancia']

    palavra = random.choice(palavras) #Escolhe ramdomicamente

    #List comprehension
    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:",chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra:").lower()

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
             chances -= 1
             letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra é:", palavra)
            break

    if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra é:", palavra)

if __name__ == '__main__':
    game()
    print("\nFinalizado!")