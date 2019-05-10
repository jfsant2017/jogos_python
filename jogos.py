import forca
import adivinhacao
import velha

def escolhe_jogo():
    exibe_menu()
    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print('Jogando Velha')
        velha.jogar()

def exibe_menu():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca")
    print("(2) Adivinhação")
    print("(3) Velha")

if(__name__ == "__main__"):
    escolhe_jogo()
