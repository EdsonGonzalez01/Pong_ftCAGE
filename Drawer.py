import pygame

class Drawer:
    '''Singleton que se encarga de crear una unica instancia de la pantalla'''

    _instance = None
    def __new__(cls) -> None:
        '''Metodo que crea la instancia unica de la pantalla en la que se dibujaran los objetos'''
        if cls._instance is None:
            pygame.init()
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        '''Constructor que define las propiedades principales de la pantalla donde se dibujaran los objetos'''
        # Set up the screen
        self.screen_width = 640
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong")
        # Set up the clock
        self.clock = pygame.time.Clock()
        self.clock.tick(60)