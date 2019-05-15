class Playlist():
    def __init__(self, nome_jogador, lista_jogos):
        self.__nome_jogador = nome_jogador
        self.__lista_jogos = lista_jogos

    @property
    def jogador(self):
        return self.__nome_jogador

    def __getitem__(self, item):
        return self.__lista_jogos[item]

    def __len__(self):
        return len(self.__lista_jogos)