from abc import ABC, abstractmethod

class Jogo(ABC):
    @abstractmethod
    def jogar(self):
        pass

    @abstractmethod
    def __init__(self, jogador):
        pass

    def continuar(self):
        return input('Deseja jogar novamente? [S|N]: ').lower().startswith('s')

    def entrada_numerica(self, mensagem):
        while True:
            try:
                numero = int(input(f'{mensagem}: '))
            except ValueError as e:
                numero = -1
            else:
                break

        return numero
