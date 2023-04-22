from GameItem import GameItem
from Drawer import Drawer
import pygame
class Player(GameItem):
    def __init__(self, type, drawer: Drawer, speed) -> None:
        super().__init__(speed)
        self.points = 0
        self.name = ""
        self.width = 15
        self.height = 60
        self.type = type # POSSIBLE VALUES: LEFT | RIGHT |  None 
        self.drawer: Drawer = drawer
        pygame.init()
        if self.type == "LEFT":
            self.posX = 25
            self.posY = (self.drawer.screen_width / 2) - (self.drawer.screen_height / 2)
        if self.type == "RIGHT":
            self.posX = self.drawer.screen_width - self.width - 25
            self.posY = (self.drawer.screen_height / 2) - (self.height / 2)            

    #def move(self):
        
    
    def draw(self):
        if self.type == "LEFT":
            pygame.draw.rect(self.drawer.screen, (255,0,0), (self.posX, self.posY, self.width, self.height))

        if self.type == "RIGHT":
            pygame.draw.rect(self.drawer.screen, (0,255,0), (self.posX, self.posY, self.width, self.height))
        
