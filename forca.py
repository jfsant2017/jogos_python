import random
import csv
from jogo import Jogo

class Forca(Jogo):
    def __init__(self, jogador):
        self.__jogador = jogador

    def __str__(self):
        return f'Forca - jogo de advinhação de palavras letra a letra!'

    def jogar(self):

        self.mensagem_boas_vindas()
        palavra_secreta = self.carrega_palavra_secreta()

        letras_acertadas = self.inicializa_letras_acertadas(palavra_secreta[0])

        enforcou = False
        acertou  = False
        erros = 0

        while (not acertou and not enforcou):

            chute = self.pede_chute()

            if (chute.upper() == 'DICA'):
                print("A dica é: {}".format(palavra_secreta[1]))
            elif (chute.upper() == 'SAIR'):
                print("Saindo....")
                erros = 7
            elif (chute in palavra_secreta[0]):
                self.marca_chute_correto(chute, letras_acertadas, palavra_secreta[0])
            else:
                erros += 1

            self.desenha_forca(erros)

            enforcou = erros == 7
            acertou = "_" not in letras_acertadas
            print(self.exibir_palavra(letras_acertadas))

        if (acertou):
            self.imprime_mensagem_vencedor()
        else:
            self.imprime_mensagem_perdedor(palavra_secreta[0])

    def mensagem_boas_vindas(self):
        print("************************************")
        print("*   Bem vindo ao jogo da Forca!    *")
        print("************************************")
        print("* Opções:                          *")
        print("*  1. Informe uma letra para chute *")
        print("*  2. Digite DICA para obter ajuda *")
        print("*  3. Digite SAIR para finalizar   *")
        print("************************************")

    def carrega_palavra_secreta(self, primeira_linha_valida = 0, nome_arquivo="palavras.txt"):
        palavras = []
        dicas = []
        with open(nome_arquivo, 'r') as arquivo:
            reader = csv.reader(arquivo, delimiter='\t')
            for palavra, dica in reader:
                palavras.append(palavra.strip())
                dicas.append(dica.strip())

        posicao = random.randrange(primeira_linha_valida, len(palavras))

        return [palavras[posicao].upper(), dicas[posicao]]

    def inicializa_letras_acertadas(self, palavra):
        return ["_" for letra in palavra]

    def pede_chute(self):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        return chute

    def marca_chute_correto(self, chute, letras_acertadas, palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1

    def imprime_mensagem_vencedor(self):
        print(f'Parabéns, {self.__jogador} você ganhou!')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def imprime_mensagem_perdedor(self, palavra_secreta):
        print(f'Puxa, {self.__jogador} você foi enforcado!')
        print(f'A palavra era {palavra_secreta}')
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def desenha_forca(self, erros):
        print("  _______     ")
        print(" |/      |    ")
        if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    def exibir_palavra(self, palavra):
        conteudo = ""
        for letra in palavra:
            conteudo = conteudo + ' ' + letra
        return conteudo

