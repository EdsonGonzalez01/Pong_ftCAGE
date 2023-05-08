from Drawable import Drawable
from Moveable import Moveable
from Drawer import Drawer
import math
class GameItem(Drawable, Moveable):
    '''Template Method: Clase abstracta que se encarga de definir el comportamiento de cualquier objeto'''
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
        '''Metodo abstracto que dibuja al GameItem'''
        pass

    def cantMoveVertically(self):
        '''Metodo que determina si un GameItem puede moverse verticalmente'''
        canMoveUp = (self.posY <= 0 and self.direction == math.pi/2)
        canMoveDown = (self.posY + self.height >= self.drawer.screen_height and self.direction == math.pi*3/2)
        return canMoveUp or canMoveDown

    def cantMoveHorizontally(self):
        '''Metodo que determina si un GameItem puede moverse horizontalmete'''
        cantMoveLeft = (self.posX <= 0 and self.direction == math.pi) 
        cantMoveRight = (self.posX + self.width >= self.drawer.screen_width and self.direction == 0)
        return cantMoveLeft or cantMoveRight

    def move(self, dir):
        '''Metodo que permite a los GameItems moverse en la pantalla'''
        self.direction = dir
        if  self.cantMoveVertically() or self.cantMoveHorizontally():
            return
        self.posY = (self.posY - math.sin(self.direction) * self.speed)
        self.posX = (self.posX + math.cos(self.direction) * self.speed)
    