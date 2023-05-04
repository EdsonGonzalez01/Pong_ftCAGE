import random
import pygame
from Drawer import Drawer
from Player import Player
from Ball import Ball
import math
from Board import Board


class GameEngine:
    '''Clase que se encarga de manejar y llevar a cabo todas las operaciones del juego'''
    def __init__(self) -> None:
        '''Constructor que inicializa la clase GameEngine'''
        self.drawer = Drawer()
        self.left = Player("LEFT", self.drawer, .51, 15,60)
        self.right = Player("RIGHT", self.drawer, .51,15,60)
        self.ball = Ball(self.drawer, .2)
        self.board = Board(self.right, self.left, self.ball)


    def runGame(self):
        '''Metodo que corre el funcionamiento principal del juego'''
        game_running = True
        print(self.drawer.screen_width)
        while game_running:
            # Handle input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.board.playerRight.move(math.pi/2)
            elif keys[pygame.K_DOWN]:
                self.board.playerRight.move(3/2*math.pi)
            if keys[pygame.K_w]:
                self.board.playerLeft.move(math.pi/2)
            elif keys[pygame.K_s]:
                self.board.playerLeft.move(math.pi/2*3)
                
            self.board.updateItems()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

            pygame.display.flip()
                
            self.drawer.screen.fill((0,0,0))
