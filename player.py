import pygame, simpleGE

class LblOutput(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 25)
        self.text = "current tile: "
        self.fgColor = "white"
        self.bgColor = "black"
        self.clearBack = True

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("red", (20, 20))
        self.moveSpeed = .5
        self.tileOver = (0,0)
        self.tileState = 0
        
    def process(self):
        
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
        #Our Target to go to
        if self.tileOver == (12,19):
            position = self.position
            self.colorRect("white", (20, 20))
            self.position = position
        else:
            position = self.position
            self.colorRect("red", (20,20))
            self.position = position
            
        #Speed on different tiles
        if self.tileState == 0:
            self.moveSpeed = 1
        elif self.tileState == 1:
            self.moveSpeed = 2
        elif self.tileState == 2:
            self.moveSpeed = .2
        else:
            self.moveSpeed = .5
            
