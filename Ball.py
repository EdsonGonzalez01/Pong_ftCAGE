from GameItem import GameItem
from Drawer import Drawer
class Ball(GameItem):
    def __init__(self, drawer: Drawer) -> None:
        super().__init__()
        self.direction = 0 # using the unit circle

    def move(self, dir):
        pass

    def draw(self):
        pass