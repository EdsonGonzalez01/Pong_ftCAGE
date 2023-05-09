from abc import ABC
class Moveable(ABC):
    '''Interfaz que declara al objeto como movible'''
    def move(self, dir)-> None:
        '''Metodo abstracto que permite a los GameItems moverse en la pantalla'''
        pass