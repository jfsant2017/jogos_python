from abc import ABC, abstractmethod

class Jogo(ABC):
    @abstractmethod
    def jogar(self):
        pass

    # @abstractmethod
    # def exibe_menu(self):
    #     pass

    @abstractmethod
    def __init__(self, jogador):
        pass
