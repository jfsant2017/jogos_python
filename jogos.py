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
    jogo = escolha_opcoes()

    if (jogo > 0 and jogo <= len(minha_playlist)):
        while True:
            minha_playlist[jogo - 1].jogar()

            exibe_menu(jogador, minha_playlist)
            jogo = escolha_opcoes()

            if (jogo == 0):
                break

            if (jogo > len(minha_playlist)):
                print('Opção inexistente.')

    else:
        print(f'Opção incorreta.')

    print(f'Adiós {jogador}!!!!!!!!!!!!!!!!!!')

    # elif(jogo == 3):
    #     print('Jogando Velha')
    #     velha.jogar()

def exibe_menu(jogador, minha_playlist):
    print(f'Olá {jogador}!!!!!!!!\n\n')

    if (len(minha_playlist) == 0):
        print("Que pena! Nenhum jogo disponível!")
    else:
        print("**************************************************************************************")
        print("*******Escolha o seu jogo!************************************************************")
        print("**************************************************************************************")
        contador = 1
        for jogo in minha_playlist:
            print(f'* Opção {contador}: {jogo}')
            contador += 1
        print("**************************************************************************************")

def escolha_opcoes():
    while True:
        try:
            numero = int(input("Escolha um jogo ou digite 0 para sair: "))
        except ValueError as e:
            numero = 0
        else:
            break

    return numero

if(__name__ == "__main__"):
    escolhe_jogo()
