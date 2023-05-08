import math
import random as rnd
from Player import Player
from Ball import Ball
from Drawer import Drawer
import numpy as np
class Board:
    '''Clase Board que contiene los objetos que se muestran en pantalla'''
    def __init__(self, playerRight, playerLeft, ball) -> None:
        '''Constructor que inicializa la clase Board'''
        self.playerRight: Player = playerRight
        self.playerLeft:Player = playerLeft
        self.ball:Ball = ball
        self.items = [playerLeft, playerRight, ball]
        self.drawer = Drawer()
    
    def checkForGoals(self):
        '''Metodo que se encarga de determinar si un gol fue anotado'''
        if(self.ball.posX <= 0):
            self.playerLeft.points += 1
            self.resetAfterGoal()
            return True
        elif(self.ball.posX + self.ball.width >= self.drawer.screen_width):
            self.playerRight.points += 1
            self.resetAfterGoal()
            return True
        return False
        

    def resetAfterGoal(self):
        '''Metodo que se encarga de resetear la posicion de los jugadores y la pelota'''
        self.playerLeft.posX = 25
        self.playerLeft.posY = (self.drawer.screen_width / 2) - (self.drawer.screen_height / 2)
        self.playerRight.posX = self.drawer.screen_width - self.playerRight.width - 25
        self.playerRight.posY = (self.drawer.screen_height / 2) - (self.playerRight.height / 2)
        self.ball.posX = self.drawer.screen_width/2
        self.ball.posY = self.drawer.screen_height/2
        
    def getRandomValueBetween0PIAnd2PI(self):
        rnd_num = rnd.random() + rnd.random() * math.pi
        return rnd_num

    def checkCollisionRightPlayerRandom(self): #if -1, then no collision
        #caso donde pega en el coco de arriba
        #caso donde pega en la parte de enfrente
        if int(self.ball.posX + self.ball.width) == self.playerRight.posX:
            if (int(self.ball.posY + self.ball.height) >= self.playerRight.posY) and (int(self.ball.posY) <= int(self.playerRight.posY + self.playerRight.height)): #hay colision
                #return randomly anything between pi/2 and 3pi/2
                rnd_num = (rnd.random() + .5) * math.pi
                return rnd_num
        #caso donde pega en el coco de abajo
        return -1
    
    def checkCollisionLeftPlayerRandom(self):#if -1, then no collision
        #caso donde pega en el coco de arriba
        #caso donde pega en la parte de enfrente
        if int(self.ball.posX) == int(self.playerLeft.posX + self.playerLeft.width):
            if (int(self.ball.posY + self.ball.height) >= self.playerLeft.posY) and (int(self.ball.posY) <= int(self.playerLeft.posY + self.playerLeft.height)): #hay colision
                #return randomly anything between pi/2 and 3pi/2 but negative
                rnd_num = (rnd.random()/2) * math.pi
                #return 1 or -1 randomly
                if (rnd.random() > .5):
                    return rnd_num * -1
                return rnd_num
        #caso donde pega en el coco de abajo
        return -1
    
    def getNormalVector(self, player: Player, ball: Ball):
        if (player.type == "RIGHT"):
            #center is <posx + width/2, posy + height/2>
            #normal vector is <posx - ball.width/2, posy + height/2>
            return (player.posX - ball.width/2, player.posY + player.height/2)
        if (player.type == "LEFT"):
            #center is <posx + width/2, posy + height/2>
            #normal vector is <posx + width/2 + ball.width/2, posy + height/2>
            return (player.posX + player.width/2 + ball.width/2, player.posY + player.height/2)
            
    def getBallVector(self, player: Player, ball: Ball):
        if (player.type == "RIGHT"):
            return (player.posX - ball.width/2, (ball.posY + ball.width) - (player.posY + player.height/2))
        if (player.type == "LEFT"):
            return (player.posX + player.width/2 + ball.width/2, (ball.posY + ball.width) - (player.posY + player.height/2))

    def dotProduct(self, nVec, bVec):
        return nVec[0]*bVec[0] + nVec[1]*bVec[1]

    def mag(self, vec):
        return math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
        
    def checkCollisionRightPlayer(self):
        if int(self.ball.posX + self.ball.width) == self.playerRight.posX:
            if (int(self.ball.posY + self.ball.height) >= self.playerRight.posY) and (int(self.ball.posY) <= int(self.playerRight.posY + self.playerRight.height)): #hay colision
                nVec = self.getNormalVector(self.playerRight, self.ball)
                bVec = self.getBallVector(self.playerRight, self.ball)
                return math.acos(self.dotProduct(nVec, bVec)/(self.mag(nVec)*self.mag(bVec)))
        return -1

    def checkCollisionLeftPlayer(self):
        if int(self.ball.posX) == int(self.playerLeft.posX + self.playerLeft.width):
            if (int(self.ball.posY + self.ball.height) >= self.playerLeft.posY) and (int(self.ball.posY) <= int(self.playerLeft.posY + self.playerLeft.height)): #hay colision
                nVec = self.getNormalVector(self.playerLeft, self.ball)
                bVec = self.getBallVector(self.playerLeft, self.ball)
                return math.acos(self.dotProduct(nVec, bVec)/(self.mag(nVec)*self.mag(bVec)))
        return -1
    
    def collidesWithUpperWall(self):
        if (self.ball.posY <= 0):
            #return randomly anything between pi and 2pi    
            rnd_num = (rnd.random() + 1) * math.pi 
            return rnd_num
        return -1
        
    def collidesWithLowerWall(self):
        if (self.ball.posY + self.ball.height >= self.drawer.screen_height):
            #return randomly anything between 0 and pi
            rnd_num = rnd.random() * math.pi
            return rnd_num
        return -1

    def getBallCollisionDirection(self):
        '''Metodo que regresa la direccion de la pelota dado que hay colision'''
        if (self.collidesWithUpperWall() != -1):
            return self.collidesWithUpperWall()
        if (self.collidesWithLowerWall() != -1):
            return self.collidesWithLowerWall()
        if (self.checkCollisionRightPlayerRandom() != -1):
            return self.checkCollisionRightPlayerRandom()
        if (self.checkCollisionLeftPlayerRandom() != -1):
            return self.checkCollisionLeftPlayerRandom()
        #no collision, keep same direction
        return self.ball.direction
    
    def updateItems(self):
        '''Dibuja/actualiza los objetos dentro la pantalla'''
        if (self.checkForGoals()):
            self.ball.move(self.getRandomValueBetween0PIAnd2PI())
        else:
            self.ball.move(self.getBallCollisionDirection())
        for item in self.items:
            item.draw()
