from GameItem import GameItem
from Drawer import Drawer
import pygame
class Ball(GameItem):
    '''Clase Pelota que implementa GameItem y se encarga de definir el funcionamiento de la pelota y la manera en como se dibuja'''
    def __init__(self, drawer: Drawer, speed) -> None:
        '''Constructor que inicializa la clase Ball'''
        super().__init__(speed)
        pygame.init()
        self.posX = drawer.screen_width/2
        self.posY = drawer.screen_height/2

    def draw(self):
        '''Metodo que se encarga de dibujar la pelota en la pantalla principal'''
        pygame.draw.rect(self.drawer.screen, self.color, (self.posX, self.posY, self.width, self.height))