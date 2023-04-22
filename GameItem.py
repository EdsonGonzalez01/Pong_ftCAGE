from Drawable import Drawable
from Moveable import Moveable
from Drawer import Drawer
import math
class GameItem(Drawable, Moveable):
    def __init__(self, speed) -> None:
        self.posX = 0
        self.posY = 0
        self.speed = speed
        self.width = 15
        self.height = 15
        self.color = (255,255,255)
        self.direction = 0
        self.drawer = Drawer()

    def draw(self):
        pass

    def cantMoveVertically(self):
        return (self.posY <= 0 and self.direction == math.pi/2) or (self.posY + self.height >= self.drawer.screen_height and self.direction == math.pi*3/2)

    def cantMoveHorizontally(self):
        valor1 = (self.posX <= 0 and self.direction == math.pi) 
        valor2 = (self.posX + self.width >= self.drawer.screen_width and self.direction == 0)
        return valor1 or valor2

    def move(self, dir):
        self.direction = dir
        if  self.cantMoveVertically() or self.cantMoveHorizontally():
            return
        self.posY = self.posY - math.sin(dir) * self.speed
        self.posX = self.posX + math.cos(dir) * self.speed
    