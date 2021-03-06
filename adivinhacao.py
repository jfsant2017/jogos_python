import random
from jogo import Jogo

class Adivinhacao(Jogo):
    def __init__(self, jogador):
        self.__jogador = jogador

    def __str__(self):
        return f'Advinhação - jogo de advinhação numérica com limite de tentativas!'

    def jogar(self):
        self.exibir_menu()
        pontos = 1000

        while True:
            self.escolher_nivel()
            numero_secreto = random.randrange(1,101)
            total_de_tentativas = 0

            # nivel = int(input("Escolha o nível: "))
            nivel = self.entrada_numerica('Escolha o nível')

            if(nivel == 1):
                total_de_tentativas = 20
                print(f'Fácil {self.__jogador}?!?!?!?! Tá com medinho???\n')
            elif(nivel == 2):
                total_de_tentativas = 10
                print(f'Hummmmm.... respeitável......\n')
            else:
                total_de_tentativas = 5
                print(f'Aêêêê {self.__jogador}!!!! El macho!!!!\n')

            acertou = False

            for rodada in range(1, total_de_tentativas + 1):
                print("Tentativa {} de {}".format(rodada, total_de_tentativas))

                # chute_str = input("Digite um número entre 1 e 100: ")
                chute_str = self.entrada_numerica('Digite um número entre 1 e 100')
                print("Você digitou " , chute_str)
                chute = int(chute_str)

                if(chute < 1 or chute > 100):
                    print("Você deve digitar um número entre 1 e 100!")
                    continue

                acertou = chute == numero_secreto
                maior   = chute > numero_secreto
                menor   = chute < numero_secreto

                if(acertou):
                    print(f'Você acertou {self.__jogador} e fez {pontos} pontos!')
                    break
                else:
                    if(maior):
                        print("Você errou! O seu chute foi maior do que o número secreto.")
                    elif(menor):
                        print("Você errou! O seu chute foi menor do que o número secreto.")
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos

            if (acertou):
                print(f'\nVocê ganhou {self.__jogador}!')
            else:
                print(f'\nVocê perdeu {self.__jogador}!')

            if (not self.continuar()):
                break

        print("Fim do jogo")
        return 0

    def exibir_menu(self):
        print("*********************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("*********************************")

    def escolher_nivel(self):
        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil\n")

