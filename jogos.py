from forca import Forca
from adivinhacao import Adivinhacao
# import velha
from playlist import Playlist

def escolhe_jogo():

    jogador = input("Qual o seu nome? ")
    jogador = jogador.title()

    forca = Forca(jogador)
    advinhacao = Adivinhacao(jogador)

    jogos_disponiveis = [ forca, advinhacao ]
    minha_playlist = Playlist(jogador, jogos_disponiveis)

    exibe_menu(jogador, minha_playlist)

    jogo = int(input("Qual jogo? "))

    if (jogo > 0):
        minha_playlist[jogo - 1].jogar()
    else:
        print('Errou!!!!!!!!!!!!!!!!!!')

    # if(jogo == 1):
    #     print("Jogando forca")
    #     forca.jogar()
    # elif(jogo == 2):
    #     print("Jogando adivinhação")
    #     adivinhacao.jogar()
    # elif(jogo == 3):
    #     print('Jogando Velha')
    #     velha.jogar()

def exibe_menu(jogador, minha_playlist):
    print(f'Olá {jogador}!!!!!!!!')

    if (len(minha_playlist) == 0):
        print("Que pena! Nenhum jogo disponível!")
    else:
        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")
        contador = 1
        for jogo in minha_playlist:
            print(f'Opção {contador}: {jogo}')
            contador += 1

if(__name__ == "__main__"):
    escolhe_jogo()
