from abc import ABC

class Drawable(ABC):
    '''Interfaz que declara al objeto como un metodo dibujable'''
    def draw(self):
        '''Metodo abstracto que dibuja al GameItem'''
        pass