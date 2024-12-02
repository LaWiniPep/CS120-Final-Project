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
        self.moveSpeed = 5
        self.tileOver = (0,0)
        self.tileState = 0
        
    def process(self):
        
#         self.correction = (0, 0)
        self.move = False
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
            self.move = True
#             if self.state == self.edge:
#                 self.correction = self.y + self.moveSpeed
            
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
            self.move = True
#             if self.scene.state == self.scene.edge:
#                 self.correction = self.y - self.moveSpeed
            
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
            self.move = True
#             if self.scene.state == self.scene.edge:
#                 self.correction = self.x + self.moveSpeed
            
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            self.move = True
#             if self.scene.state == self.scene.edge:
#                 self.correction = self.x - self.moveSpeed
                
#         barrier = self.scene.barrier
#         if self.collidesWith(barrier):
#             self.x += self.correction
#             self.y += self.correction    
            
        #Speed on different tiles
        if self.tileState == 0:
            self.moveSpeed = 1.5
        elif self.tileState == 1:
            self.moveSpeed = 3
        elif self.tileState == 2:
            self.moveSpeed = .2
        else:
            self.moveSpeed = 2
#             
