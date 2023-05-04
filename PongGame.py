from GameEngine import GameEngine

class PongGame:
    '''Clase Principal que crea el GameEngine que s eencargara de correr nuestro juego'''
    def __init__(self):
        self.game = GameEngine()
        self.game.runGame()
        

'''Codigo del cliente que corre el juego'''
if __name__ == "__main__":
    game = PongGame()