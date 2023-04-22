import pygame

class Drawer:

    _instance = None

    def _new_(cls) -> None:
        if cls._instance is None:
            with pygame.init():
                cls._instance = super().new_(cls)
        return cls._instance
    
    def __init__(self) -> None:
        # Set up the screen
        self.screen_width = 640
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong")
        # Set up the clock
        self.clock = pygame.time.Clock()
        self.clock.tick(60)