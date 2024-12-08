import pygame
import simpleGE
from CoPilotPlayer import Player, LblOutput

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
        if self.clicked:
            newState = self.state + 1
            if newState > 2:
                newState = 0
            self.setState(newState)

        if self.collidesWith(self.scene.player):
            stateInfo = self.stateName[self.state]
            self.scene.player.tileOver = self.tilePos
            self.scene.player.tileState = self.state
            rowCol = f"{self.tilePos[0]}, {self.tilePos[1]}"
            self.scene.lblOutput.text = f"{stateInfo} {rowCol}"

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Click on a tile to edit, arrows to move")
        
        self.WINDOW_WIDTH = 640  # Adjust as necessary
        self.WINDOW_HEIGHT = 480  # Adjust as necessary

        self.offRow = 0
        self.offCol = 0

        # Start with the top-left map
        self.loadTopLeftMap()

        self.player = Player(self)
        self.lblOutput = LblOutput()

        self.sprites = [self.player, self.lblOutput]

    def tileMap(self):
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
        
        if self.tileset == [row[:20]for row in self.tileMap[:15]]:
            direction = topLeft
 
        elif self.tileset == [row[20:]for row in self.tileMap[:15]]:
            direction = topRight
      
        elif self.tileset == [row[20]for row in self.tileMap[15:]]:
            direction = bottomLeft
      
        elif self.tileset == [row[20:]for row in self.tileMap[15:]]:
            direction = bottomRight
        else:
            direction = topLeft
            
    def loadTopLeftMap(self):
        self.tileset = [row[:20]for row in self.tileMap[:15]]
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
                
    def showMap(self):
        """ shows a subset of the map SCREEN_ROWS by SCREENCOLS
            offset by offRow, offCol """
            
        for row in range(self.SCREEN_ROWS):
            for col in range(self.SCREEN_COLS):
                currentVal = self.tileMap[row + self.offRow][col + self.offCol]
                self.tileset[row][col].setState(currentVal)


    def switchMap(self, direction):
        if direction == "left":
            # Assuming top_left and top_right transition
            if self.currentMap == "topRight":
                self.currentMap = "topLeft"
                self.loadTopLeftMap()
                self.player.x = self.WINDOW_WIDTH - self.player.width
            elif self.currentM<ap == "bottomRight":
                self.currentMap = "bottomLeft"
                self.loadBottomLeftMap()
                self.player.x = self.WINDOW_WIDTH - self.player.width
        elif direction == "right":
            if self.currentMap == "topLeft":
                self.currentMap = "topRight"
                self.loadTopRightMap()
                self.player.x = 0
            elif self.currentMap == "bottomLeft":
                self.currentMap = "bottomRight"
                self.loadBottomRightMap()
                self.player.x = 0
        elif direction == "up":
            if self.currentMap == "bottomLeft":
                self.currentMap = "topLeft"
                self.loadTopLeftMap()
                self.player.y = self.WINDOW_HEIGHT - self.player.height
            elif self.currentMap == "bottomRight":
                self.currentMap = "topRight"
                self.loadTopRightMap()
                self.player.y = self.WINDOW_HEIGHT - self.player.height
        elif direction == "down":
            if self.currentMap == "topLeft":
                self.currentMap = "bottomLeft"
                self.loadBottomLeftMap()
                self.player.y = 0
            elif self.currentMap == "topRight":
                self.currentMap = "bottomRight"
                self.loadBottomRightMap()
                self.player.y = 0
                

#     def loadTopLeftMap(self):
#         if
#         self.currentMap = "topLeft"
# 
#     def loadTopRightMap(self):
#         loadTopRightMap(self)
#         self.currentMap = "topRight"
# 
#     def loadBottomLeftMap(self):
#         load_bottom_left_map(self)
#         self.currentMap = "bottomLeft"
# 
#     def loadBottomRightMap(self):
#         loadBottomRightMap(self)
#         self.currentMap = "bottomRight"

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
