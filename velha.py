import os
import random
import time
from jogo import Jogo

class Velha(Jogo):

    def __init__(self, jogador):
        self.__jogador = jogador

    def __str__(self):
        return f'Jogo da Velha - o famoso Tic Tac Toe!'

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self, board):
        self.clear()
        print('   |   |')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('   |   |')

    def player_input(self):
        marker = ' '
        while not (marker == 'X' or marker == 'O'):
            print("*********************************")
            marker = input('Jogador Nº1 \nVocê quer ser X ou O?: ').upper()
            print("*********************************")

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    def place_marker(self, board, marker, position):
        board[position] = marker

    def win_check(self, board, mark):
        return ((board[6] == mark and board[7] == mark and board[8] == mark) or  # vitória pelo topo
                # pelo meio
                (board[3] == mark and board[4] == mark and board[5] == mark) or
                # por baixo
                (board[0] == mark and board[1] == mark and board[2] == mark) or
                # pela esquda
                (board[6] == mark and board[3] == mark and board[0] == mark) or
                # pelo meio
                (board[7] == mark and board[4] == mark and board[1] == mark) or
                # pela direita
                (board[8] == mark and board[5] == mark and board[2] == mark) or
                # diagonal
                (board[6] == mark and board[4] == mark and board[2] == mark) or
                (board[8] == mark and board[4] == mark and board[0] == mark))  # diagonal


    def choose_first(self):
        if random.randint(0, 1) == 0:
            return 'Jogador 2'
        else:
            return 'Jogador 1'


    def space_check(self, board, position):
        return board[position - 1] == " "


    def full_boolean_check(self, board):
        for i in range(1, 9):
            if self.space_check(board, i):
                return False
        return True

    def player_choice(self, board):
        position = ' '
        while position not in '1 2 3 4 5 6 7 8 9'.split() or not self.space_check(board, int(position)):
            position = input('Escolha sua jogada (1-9): ')

        return int(position)

    def jogar(self):
        print("*********************************")
        print('Bem vindo ao jogo da velha!')
        print("*********************************")
        while True:
            board = [' '] * 9
            player1_marker, player2_marker = self.player_input()  # Desempacotamento de tuplas
            turn = self.choose_first()
            print(turn + ' É O PRIMEIRO A JOGAR!\n\n\n\n')
            print('PREPAREM-SE...')
            print('Loading.......................')
            time.sleep(3)

            game_on = True

            while game_on:
                if turn == 'Jogador 1':
                    self.display_board(board)
                    position = self.player_choice(board) - 1
                    self.place_marker(board, player1_marker, position)

                if self.win_check(board, player1_marker):
                    self.display_board(board)
                    print("Parabéns %s, você ganhou!" % (turn))
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
                    game_on = False
                else:
                    if self.full_boolean_check(board):
                        self.display_board(board)
                        print("Empate!!!")
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
                        break
                    else:
                        turn = 'Jogador 2'

                if turn == 'Jogador 2':
                    self.display_board(board)
                    position = self.player_choice(board) - 1
                    self.place_marker(board, player2_marker, position)

                if self.win_check(board, player2_marker):
                    self.display_board(board)
                    print("Parabéns %s, você ganhou!" % (turn))
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
                    game_on = False
                else:
                    if self.full_boolean_check(board):
                        self.display_board(board)
                        print("Empate!!!")
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
                        break
                    else:
                        turn = 'Jogador 1'

            if (not self.continuar()):
                break
