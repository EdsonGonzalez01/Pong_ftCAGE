from GameItem import GameItem
from Drawer import Drawer
import pygame
class Ball(GameItem):
    def __init__(self, drawer: Drawer, speed) -> None:
        super().__init__(speed)
        pygame.init()
        self.posX = drawer.screen_width/2
        self.posY = drawer.screen_height/2




    #def move(self, dir):
        #pass

    def draw(self):
        pygame.draw.rect(self.drawer.screen, self.color, (self.posX, self.posY, self.width, self.height))