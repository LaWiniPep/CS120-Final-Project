import pygame, simpleGE
from player import Player, LblOutput

""" tileScroll.py
    demonstrate basic tbw 
    tile images from lpc Atlas - openGameArt
    http://opengameart.org/content/lpc-tile-atlas
"""
    
class Tile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("Grass32.png"),
            pygame.image.load("Path.png"),
            pygame.image.load("Water.png"),
            pygame.image.load("Door.png"),
            pygame.image.load("Edge.png"),
            pygame.image.load("CaveDoor.png")]
        
        self.stateName = ["grass", "path", "water", "door", "edge", "cave door"]
        
        self.setSize(32, 32)
        self.GRASS = 0
        self.DIRT = 1
        self.WATER = 2
        self.DOOR = 3
        self.edge = 4
        self.CAVEDOOR = 5
        self.state = self.GRASS
        
        
    
    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])
        
    def process(self):
        
        #allow editing
        if self.clicked:
            newState = self.state + 1
            if newState > 2:
                newState = 0
            self.setState(newState)         
        
        # look for player
        if self.collidesWith(self.scene.player):
            stateInfo = self.stateName[self.state]
            self.scene.player.tileOver = self.tilePos
            self.scene.player.tileState = self.state
            rowCol = f"{self.tilePos[0]}, {self.tilePos[1]}"
            
            self.scene.lblOutput.text = f"{stateInfo} {rowCol}"
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("The Legend of Alex")
        
        self.WINDOW_WIDTH = 640 #Can Adjust
        self.WINDOW_HEIGHT = 480 #Can Adjust
        self.tileset = []
        
        self.ROWS = 30
        self.COLS = 42
        
        self.SCREEN_ROWS = 15
        self.SCREEN_COLS = 20
        
        self.offRow = 0
        self.offCol = 0
        
        self.loadTopLeftMap()
        
        self.player = Player(self)
        self.lblOutput = LblOutput()
        
        self.sprites = [tile for row in self.tileset for tile in row] + [self.player, self.lblOutput]
        
    def switchMap(self, direction):
        if direction == "left":
            
            self.loadTopLeftMap()
        elif quadrant == "topRight":
            self.loadTopRightMap()
        elif quadrant == "bottomLeft":
            self.loadBottomLeftMap()
        elif quadrant == "bottomRight":
            self.loadBottomRightMap()
            
    def loadTopRightMap(self):
        self.loadTopRightMap(self)
    def loadTopLeftMap(self):
        self.loadTopLeftMap(self)
    def loadBottomRightMap(self):
        self.loadBottomRightMap(self)
    def loadBottomLeftMap(self):
        self.loadBottomLeftMap(self)
        
        
        self.sprites = [self.tileset, self.player, self.lblOutput]
    def loadMap(self):
        self.tileMap = [
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],  
            [4,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4],  
            [4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4],  
            [4,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,4,4,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,4,4,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,4],  
            [4,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,4],  
            [4,0,2,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,4],
            [4,0,2,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,4],  
            [4,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,4],  
            [4,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,4],  
            [4,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,5,2,0,4],  
            [4,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,2,2,0,4],  
            [4,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
]
      
        if self.lblOutput == [row[:20]for row in self.tileMap[:15]]:
            quadrant = topLeft
 
        elif self.lblOutput == [row[20:]for row in self.tileMap[:15]]:
            qaudrant = topRight
      
        elif self.lblOutput == [row[20]for row in self.tileMap[15:]]:
            quadrant = bottomLeft
      
        elif self.lblOutput == [row[20:]for row in self.tileMap[15:]]:
            quadrant = bottomRight
        else:
            quadrant = topLeft

      
      
    def loadTopLeftMap(self):
          self.tileset = []
          for row in range(len(topLeft)):
              self.tileset.append([])
              for col in range(len(topLeft[row])):
                  currentVal = topLeft[row][col]
                  newTile = Tile(self)
                  newTile.setState(currentVal)
                  newTile.tilePos = (row,col)
                  xPos = 16 + (32 * col)
                  yPos = 16 + (32 * row)
                  newTile.x = xPos
                  newTile.y = yPos
                  self.tileset[row].append(newTile)
                  
    def loadTopRightMap(self):
        self.tileset = []
        for row in range(len(topRight)):
            self.tileset.append([])
            for col in range(len(topRight[row])):
                currentVal = topRight[row][col]
                newTile = Tile(self)
                newTile.setState(currentVal)
                newTile.tilePos = (row,col)
                xPos = 16 + (32 * col)
                yPos = 16 + (32 * row)
                newTile.x = xPos
                newTile.y = yPos
                self.tileset[row].append(newTile)
                
    def loadBottomLeftMap(self):
        self.tileset = []
        for row in range(len(bottomLeft)):
            self.tileset.append([])
            for col in range(len(bottomLeft)):
                currentVal = bottomLeft[row][col]
                newTile = Tile(self)
                newTile.setState(currentVal)
                newTile.tilePos = (row,col)
                xPos = 16 + (32 * col)
                yPos = 16 + (32 * row)
                newTile.x = xPos
                newTile.y = yPos
                self.tileset[row].append(newTile)
                
    def loadBottomRightMap(self):
        self.tileset = []
        for row in range(len(bottomRight)):
            self.tileset.append([])
            for col in range(len(bottomRight)):
                currentVal = bottomRight[row][col]
                newTile = Tile(self)
                newTile.setState(currentVal)
                newTile.tilePos = (row,col)
                xPos = 16 + (32 * col)
                yPos = 16 + (32 * row)
                newTile.x = xPos
                newTile.y = yPos
                self.tileset[row].append(newTile)
              
      
      
#           for col in range(self.SCREEN_COLS):
#             currentVal = self.map[row][col]
#             newTile = Tile(self)
#             newTile.setState(currentVal)
#             newTile.tilePos = (row,col)
#             xPos = 16 + (32 * col)
#             yPos = 16 + (32 * row)
#             newTile.x = xPos
#             newTile.y = yPos
#             self.tileset[row].append(newTile)
            
    def showMap(self):
        """ shows a subset of the map SCREEN_ROWS by SCREENCOLS
            offset by offRow, offCol """
            
        for row in range(self.SCREEN_ROWS):
            for col in range(self.SCREEN_COLS):
                currentVal = self.tileMap[row + self.offRow][col + self.offCol]
                self.tileset[row][col].setState(currentVal)
#                 
#     def process(self):
#         if self.isKeyPressed(pygame.K_a):
#             if self.offCol > 0:
#                 self.offCol -= 1
# #                 if self.y > 0:
# #                     self.player.tilePos 
#                     
#         if self.isKeyPressed(pygame.K_d):
#             if self.offCol < self.COLS - self.SCREEN_COLS:
#                 self.offCol += 1
# #                 if self.y < self.COLS - self.SCREEN_COLS:
# #                     self.y -= 1
#                 
#         if self.isKeyPressed(pygame.K_w):
#             if self.offRow > 0:
#                 self.offRow -= 1 
#                 
#                 
#         if self.isKeyPressed(pygame.K_s):
#             if self.offRow < (self.ROWS - self.SCREEN_ROWS):
#                 self.offRow += 1 
#                 
#         self.showMap()
        
def main():
    game = Game()
    game.start()
   
    
if __name__ == "__main__":
    main()
    