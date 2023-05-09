from GameItem import GameItem
from Drawer import Drawer
import pygame
class Player(GameItem):
    '''Clase Jugador que implementa GameItem que se encarga de definir los atributos del jugador y sobreescribir la manera en como se'''
    def __init__(self, type, drawer: Drawer, speed, width, height) -> None:
        '''Constructor de jugador que inicializa la clase con sus atributos principales'''
        super().__init__(speed)
        self.points = 0
        self.name = ""
        self.type = type # POSSIBLE VALUES: LEFT | RIGHT |  None 
        self.drawer: Drawer = drawer
        self.width = width
        self.height = height
        pygame.init()
        if self.type == "LEFT":
            self.posX = 25
            self.posY = (self.drawer.screen_width / 2) - (self.drawer.screen_height / 2)
        if self.type == "RIGHT":
            self.posX = self.drawer.screen_width - self.width - 25
            self.posY = (self.drawer.screen_height / 2) - (self.height / 2)           
        
    
    def draw(self)-> None:
        '''Metodo que se encarga de dibujar la pelota en la pantalla principal'''
        font = pygame.font.Font('freesansbold.ttf', 32)
        
        if self.type == "LEFT":
            text = font.render(str(self.points), True, (0,0,255), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (self.drawer.screen_width - 50, 50)
            self.drawer.screen.blit(text, textRect)
            pygame.draw.rect(self.drawer.screen, (255,0,0), (self.posX, self.posY, self.width, self.height))
        if self.type == "RIGHT":
            text = font.render(str(self.points), True, (0,0,255), (0,0,0))
            textRect = text.get_rect()
            textRect.center = (50, 50)
            self.drawer.screen.blit(text, textRect)
            pygame.draw.rect(self.drawer.screen, (0,255,0), (self.posX, self.posY, self.width, self.height))
            


        
