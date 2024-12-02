import pygame, simpleGE
from player_working import Player, LblOutput

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
            pygame.image.load("CaveDoor.png"),
            pygame.image.load("Stairs.png"),
            pygame.image.load("intDungeonDoorW.png"),
            pygame.image.load("intDungeonDoorE.png"),
            pygame.image.load("edgeT.png"),
            pygame.image.load("edgeB.png"),
            pygame.image.load("edgeR.png"),
            pygame.image.load("edgeL.png"),]
        
        self.stateName = ["grass", "path", "water", "door", "edge", "cave door", "stairs", "Dun doorW", "Dun DoorE", "edge T", "edge B", "edge R", "edge L"]
        
        self.setSize(32, 32)
        self.GRASS = 0
        self.DIRT = 1
        self.WATER = 2
        self.DOOR = 3
        self.edge = 4
        self.CAVEDOOR = 5
        self.STAIRS = 6
        self.INTDUNGEONDOORW = 7
        self.INTDUNGEONDOORE = 8
        self.edgeT = 9
        self.edgeB = 10
        self.edgeR = 11
        self.edgeL = 12
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
        self.tileset = []
        
        self.ROWS = 30
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
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,11],
            [4,10,10,10,10,10,10,10,10,1,10,10,10,10,10,10,10,10,10,4]
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
                
        
        self.map1 = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,11],
            [4,10,10,10,10,10,10,10,10,1,10,10,10,10,10,10,10,10,10,4]
]
        self.map2 = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11],
            [12,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,11],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,11],
            [4,10,10,10,10,10,10,10,10,10,1,10,10,10,10,10,10,10,10,4]
]
        self.map3 = [
            [9,9,9,9,9,9,9,9,9,1,9,9,9,9,9,9,9,9,9,9],  
            [12,0,2,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,2,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,11],  
            [12,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,11],  
            [12,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1],  
            [12,0,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,11],
            [12,0,2,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],  
            [12,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]
        self.map4 = [
            [9,9,9,9,9,9,9,9,9,9,1,9,9,9,9,9,9,9,9,9],  
            [12,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,11],  
            [12,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,11],  
            [12,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,11],  
            [1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,11],  
            [12,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,11],
            [12,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,11],  
            [12,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,11],  
            [12,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,11],  
            [12,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,5,2,0,11],  
            [12,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,2,2,0,11],  
            [12,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [2,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]
        self.village = [
            [9,9,9,9,9,9,9,9,9,6,9,9,9,9,9,9,9,9,9,9],
            [12,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,11],
            [12,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,11],
            [12,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,11],
            [12,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]
        self.cave = [
            [9,9,6,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]
        
        self.caveRoom = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]

            
            
    def showMap(self):
        """ shows a subset of the map SCREEN_ROWS by SCREENCOLS
            offset by offRow, offCol """
            
        for row in range(self.SCREEN_ROWS):
            for col in range(self.SCREEN_COLS):
                currentVal = self.map[row + self.offRow][col + self.offCol]
                self.tileset[row][col].setState(currentVal)

    def process(self):
        #TopL to BottomL
        if self.player.tileOver == (14,9) and self.map == self.map1:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map3
            self.player.position = (300, 35)
        #BottomL to TopL    
        elif self.player.tileOver == (0,9) and self.map == self.map3:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map1
            self.player.position = (300, 435)
            
        #TopL to TopR    
        elif self.player.tileOver == (9,19) and self.map == self.map1:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.psoition = position
            self.map = self.map2
            self.player.position = (35,300)
            
        #TopR to TopL    
        elif self.player.tileOver == (9,0) and self.map == self.map2:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map1
            self.player.position = (590, 300)
            
        #BottomL to Bottom R    
        elif self.player.tileOver == (4,19) and self.map == self.map3:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map4
            self.player.position = (35, 145)
        
        #BottomR to BottomL
        elif self.player.tileOver == (4,0) and self.map == self.map4:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map3
            self.player.position = (590, 145)
            
        #BottomR to TopR
        elif self.player.tileOver == (0,10) and self.map == self.map4:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map2
            self.player.position = (330, 435)
            
        #TopR to BottomR
        elif self.player.tileOver == (14,10) and self.map == self.map2:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map4
            self.player.position = (330, 35)
            
        #Door on map1
        elif self.player.tileOver == (1,2) and self.map == self.map1:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.village
            self.player.position = (250, 155)
            
        #Exit Village
        elif self.player.tileOver == (0,9) and self.map == self.village:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map1
            self.player.position = (80, 75)
            
        #Dungeon
        elif self.player.tileOver == (9,16) and self.map == self.map4:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.cave
            self.player.position = (80, 75)
        
        #Exit Cave
        elif self.player.tileOver == (0,2) and self.map == self.cave:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.map4
            self.player.position = (500, 300)
            
        #Cave Room
        elif self.player.tileOver == (4,0) and self.map == self.cave:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.caveRoom
            self.player.position = (595, 145)
            
        #Exit Cave Room
        elif self.player.tileOver == (4,19) and self.map == self.caveRoom:
            position = self.player.position
            self.player.colorRect("white", (20, 20))
            self.player.position = position
            self.map = self.cave
            self.player.position = (45, 145) 
        
        
#             
        else:
            position = self.player.position
            self.player.colorRect("red", (20,20))
            self.player.position = position

                
        self.showMap()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    