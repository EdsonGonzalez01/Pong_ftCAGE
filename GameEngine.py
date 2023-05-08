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
        self.left = Player("LEFT", self.drawer, 1, 15,60)
        self.right = Player("RIGHT", self.drawer, 1,15,60)
        self.ball = Ball(self.drawer, 1)
        self.board = Board(self.right, self.left, self.ball)


    def runGame(self):
        '''Metodo que corre el funcionamiento principal del juego'''
        game_running = "None"
        while game_running == "None":
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
                
            game_running = self.board.updateItems()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = "QUIT"

            pygame.display.flip()
                
            self.drawer.screen.fill((0,0,0))

            

        font = pygame.font.Font('freesansbold.ttf', 32)
        text_surface = font.render("Game Over", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.drawer.screen_width//2, self.drawer.screen_height//2))
        self.drawer.screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        

