import random
import pygame
from Drawer import Drawer
from Player import Player
from Ball import Ball
import math

drawer = Drawer()
left = Player("LEFT", drawer, .51)
right = Player("RIGHT", drawer, .51)
ball = Ball(drawer)
game_running = True
print(drawer.screen_width)
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        right.move(math.pi/2)
    elif keys[pygame.K_DOWN]:
        right.move(3/2*math.pi)
    if keys[pygame.K_w]:
        left.move(math.pi/2)
    elif keys[pygame.K_s]:
        left.move(math.pi/2*3)
    ball.move()
    left.draw()
    right.draw()
    pygame.display.flip()
        
    drawer.screen.fill((0,0,0))

#SI