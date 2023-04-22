import random
import pygame
from Drawer import Drawer
from Player import Player
from Ball import Ball
import math
from Board import Board

drawer = Drawer()
left = Player("LEFT", drawer, .51, 15,60)
right = Player("RIGHT", drawer, .51,15,60)
ball = Ball(drawer, .2)
board = Board(right, left, ball)

game_running = True
print(drawer.screen_width)
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        board.playerRight.move(math.pi/2)
    elif keys[pygame.K_DOWN]:
        board.playerRight.move(3/2*math.pi)
    if keys[pygame.K_w]:
        board.playerLeft.move(math.pi/2)
    elif keys[pygame.K_s]:
        board.playerLeft.move(math.pi/2*3)
    ball.move(0)

    board.updateItems()

    pygame.display.flip()
        
    drawer.screen.fill((0,0,0))

#SI