from Player import Player
from Ball import Ball
class Board:
    def __init__(self, playerRight, playerLeft, ball) -> None:
        self.playerRight: Player = playerRight
        self.playerLeft:Player = playerLeft
        self.ball:Ball = ball
        self.items = [playerLeft, playerRight, ball]
    
    def checkForGoals():
        pass

    def checkForBallCollition():
        pass
    
    def updateItems(self):
        for item in self.items:
            item.draw()
