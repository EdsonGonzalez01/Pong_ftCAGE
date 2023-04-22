from Drawable import Drawable
from Moveable import Moveable
import math
class GameItem(Drawable, Moveable):
    def __init__(self, speed) -> None:
        self.posX = 0
        self.posY = 0
        self.speed = speed
        self.color = (255,255,255)
        self.direction = 0

    def draw(self):
        pass

    def move(self, dir):
        self.direction = dir
        self.posY = self.posY - math.sin(dir) * self.speed
        self.posX = self.posX + math.cos(dir) * self.speed
    