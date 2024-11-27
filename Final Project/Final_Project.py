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
            pygame.image.load("Water.png")]
        
        self.stateName = ["grass", "path", "water"]
        
        self.setSize(32, 32)
        self.GRASS = 0
        self.DIRT = 1
        self.WATER = 2
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
        self.setCaption("arrows to scroll map")
        self.tileset = []
        
        self.ROWS = 20
        self.COLS = 40
        
        self.SCREEN_ROWS = 15
        self.SCREEN_COLS = 20
        
        self.offRow = 0
        self.offCol = 0
        
        self.loadMap()
        
        self.player = Player(self)
        self.lblOutput = LblOutput()
        
        self.sprites = [self.tileset, self.player, self.lblOutput]
        
    def loadMap(self):
        
      self.map = [
          
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [2,2,2,2,2,2,0,0,0,0,1,0,0,0,0,0,2,2,2,2,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,2,2,2,2,2,2,0,0,0,1,0,0,0,2,2,2,2,2,0,0,0,0,0,2,2,0,0,1,1,1,1,1,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,1,1,1,0,0,0,0],  
          [0,0,0,0,0,0,0,2,2,2,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,1,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,1,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,1,1],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
      ]
    
      for row in range(self.SCREEN_ROWS):
          self.tileset.append([])
          for col in range(self.SCREEN_COLS):
            currentVal = self.map[row][col]
            newTile = Tile(self)
            newTile.setState(currentVal)
            newTile.tilePos = (row,col)
            xPos = 16 + (32 * col)
            yPos = 16 + (32 * row)
            newTile.x = xPos
            newTile.y = yPos
            self.tileset[row].append(newTile)
            
    def showMap(self):
        """ shows a subset of the map SCREEN_ROWS by SCREENCOLS
            offset by offRow, offCol """
            
        for row in range(self.SCREEN_ROWS):
            for col in range(self.SCREEN_COLS):
                currentVal = self.map[row + self.offRow][col + self.offCol]
                self.tileset[row][col].setState(currentVal)
                
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.offCol > 0:
                self.offCol -= 1
                
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.offCol < self.COLS - self.SCREEN_COLS:
                self.offCol += 1
                
        if self.isKeyPressed(pygame.K_UP):
            if self.offRow > 0:
                self.offRow -= 1
                
        if self.isKeyPressed(pygame.K_DOWN):
            if self.offRow < (self.ROWS - self.SCREEN_ROWS):
                self.offRow += 1
                
        self.showMap()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()