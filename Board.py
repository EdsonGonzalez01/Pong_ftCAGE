import math
from Player import Player
from Ball import Ball
class Board:
    '''Clase Board que contiene los objetos que se muestran en pantalla'''
    def __init__(self, playerRight, playerLeft, ball) -> None:
        '''Constructor que inicializa la clase Board'''
        self.playerRight: Player = playerRight
        self.playerLeft:Player = playerLeft
        self.ball:Ball = ball
        self.items = [playerLeft, playerRight, ball]
    
    def checkForGoals():
        '''Metodo que se encarga de determinar si un gol fue anotado'''
        pass

    def checkCollitionLeftPlayer(self):
            '''Metodo que checa la colision del jugador de la izquierda'''
            #return self.ball.direction+math.pi
            return (self.ball.posX >= self.playerLeft.posX and self.ball.posX <= self.playerLeft.posX + self.playerLeft.width ) and (self.ball.posY >= self.playerLeft.posY and self.ball.posY <= self.playerLeft.posY + self.playerLeft.height)
    def checkCollitionRightPlayer(self):
            '''Metodo que checa la colision del jugador de la derecha'''
            #return self.ball.direction+math.pi
            return (self.ball.posX + self.ball.width >= self.playerRight.posX and self.ball.posX + self.ball.width <= self.playerRight.posX + self.playerRight.width ) and (self.ball.posY >= self.playerRight.posY and self.ball.posY <= self.playerRight.posY + self.playerRight.height)

    def checkForBallCollition(self):
        '''Metodo que checa la colision de la pelota'''
        #print(self.ball.direction)
        if self.checkCollitionRightPlayer():
            return self.ball.direction+math.pi
        elif self.checkCollitionLeftPlayer():
            return self.ball.direction-math.pi
        return self.ball.direction
    
    def updateItems(self):
        '''Dibuja/actualiza los objetos dentro la pantalla'''
        self.ball.move(self.checkForBallCollition())
        for item in self.items:
            item.draw()
