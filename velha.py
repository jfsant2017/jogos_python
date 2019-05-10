import os
import random
import time


def jogar():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    def display_board(board):
        clear()
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    # display_board([" "," "," "," ","X","O"," "," "," "," ",])


    def player_input():
        marker = ' '
        while not (marker == 'X' or marker == 'O'):
            print("*********************************")
            marker = input('Jogador Nº1 \nVocê quer ser X ou O?: ').upper()
            print("*********************************")

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


    def place_marker(board, marker, position):
        board[position] = marker


    def win_check(board, mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # vitória pelo topo
                # pelo meio
                (board[4] == mark and board[5] == mark and board[6] == mark) or
                # por baixo
                (board[1] == mark and board[2] == mark and board[3] == mark) or
                # pela esquda
                (board[7] == mark and board[4] == mark and board[1] == mark) or
                # pelo meio
                (board[8] == mark and board[5] == mark and board[2] == mark) or
                # pela direita
                (board[9] == mark and board[6] == mark and board[3] == mark) or
                # diagonal
                (board[7] == mark and board[5] == mark and board[3] == mark) or
                (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


    def choose_first():
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'


    def space_check(board, position):
        return board[position] == " "


    def full_boolean_check(board):
        for i in range(0, 10):
            if space_check(board, i):
                return False
        return True


    def player_choice(board):
        position = ' '
        while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
            position = input('Escolha sua jogada (1-9): ')

        return int(position)


    def replay():
        return input('Deseja jogar novamente? [S|N]: ').lower().startswith('s')


    print("*********************************")
    print('Bem vindo ao jogo da velha!')
    print("*********************************")
    while True:
        board = [' '] * 10
        player1_marker, player2_marker = player_input()  # Desempacotamento de tuplas
        turn = choose_first()
        print(turn + ' É O PRIMEIRO A JOGAR!\n\n\n\n')
        print('PREPAREM-SE...')
        print('Loading.......................')
        time.sleep(3)

        game_on = True

        while game_on:
            if turn == 'Player 1':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
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
                if full_boolean_check(board):
                    display_board(board)
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
                    turn = 'Player 2'

            if turn == 'Player 2':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
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
                if full_boolean_check(board):
                    display_board(board)
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
                    turn = 'Player 1'

        if not replay():
            break
if(__name__ == "__main__"):
    jogar()