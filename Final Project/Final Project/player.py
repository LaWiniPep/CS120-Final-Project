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
        keepGoing = False
        
        if self.isKeyPressed(pygame.K_UP):
            if self.y > 0:
                self.y -= self.moveSpeed
            elif self.scene.offRow > 0:
                self.scene.offRow -= 1
                self.y = self.scene.WINDOW_HEIGHT - self.height
            else:
                self.scene.switchMap("up")
                keepGoing = True
            
        if self.isKeyPressed(pygame.K_DOWN):
            if self.y < self.scene.WINDOW_HEIGHT - self.height:
                self.y += self.moveSpeed
            elif self.scene.offRow < self.scene.ROWS - self.scene.SCREEN_ROWS:
                self.scene.offRow += 1
                self.y = 0
            else:
                self.scene.switchMap("down")
                keepGoing = True
                
        if self.isKeyPressed(pygame.K_LEFT):
            if self.x > 0:
                self.x -= self.moveSpeed
            elif self.scene.offCol > 0:
                self.scene.offCol -= 1
                self.x = self.scene.WINDOW_WIDTH -self.width
            else:
                self.scene.switchMap("left")
                keepGoing = True
            
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.x < self.scene.WINDOW_WIDTH -self.width:
                self.x += self.moveSpeed
            elif self.scene.offCol < self.scene.COLS - self.scene.SCREEN_ROWS:
                self.scene.offRow += 1
                self.y = 0
            else:
                self.scene.switchMap("down")
                keepgoing = True
            
        if keepGoing == True:
            self.scene.showMap()
            
        #Village?
        if self.tileOver == (1,2):
            position = self.position
            self.colorRect("white", (20, 20))
            self.position = position
        else:
            position = self.position
            self.colorRect("red", (20,20))
            self.position = position
            
#     def process(self):
#          
#         #Exit map 1
#         if self.tileOver == (9,14) or self.tileOver == (10,14):
#             position = self.position
#             self.colorRect("white", (20,20))
#             self.position = position
#         else:
#             position = self.position
#             self.colorRect("red", (20,20))
#             self.position = position
            
        #Dungeon
            
        
            
#         #Speed on different tiles
#         if self.tileState == 0:
#             self.moveSpeed = 1
#         elif self.tileState == 1:
#             self.moveSpeed = 2
#         elif self.tileState == 2:
#             self.moveSpeed = .2
#         else:
#             self.moveSpeed = .5



            
