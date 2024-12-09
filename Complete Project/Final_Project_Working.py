import pygame, simpleGE
from player_working import *
from paths import *
from Credits import *

"""

"""

#         
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
            pygame.image.load("edgeL.png"),
            pygame.image.load("Fish.png"),
            pygame.image.load("QuigBomb.png"),
            pygame.image.load("Paul.png"),
            pygame.image.load("Credits.png"),
            pygame.image.load("Villager.png")
        ]
        self.stateName = ["grass", "path", "water", "door", "edge", "cave door", "stairs", "Dun doorW", "Dun DoorE", "edge T", "edge B", "edge R", "edge L", "Fish", "Bomb", "Paul", "Credits", "Villager"]
        
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
        self.fish = 13
        self.quigBomb = 14
        self.Paul = 15
        self.credits = 16
        self.villager = 17
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
        
        self.lblHealth = LblHealth(self)
        

        self.offRow = 0
        self.offCol = 0
        
        self.loadMap()
        
        self.enemy = Enemy(self)
        pointList = (
            (437, 81),
            (545, 111),
            (480, 123),
            (428, 74),
            (389, 133),
            (430, 155),
            (483, 123),
            (425, 65),
            (367, 65)
)
        if self.map == self.map1:
            pointList = (
                (437, 81),
                (545, 111),
                (480, 123),
                (428, 74),
                (389, 133),
                (430, 155),
                (483, 123),
                (425, 65),
                (367, 65)
)
        if self.map == self.map2:
            pointList = (
                (200, 295),
                (250, 251),
                (300, 322),
                (185, 294),
                (296, 237),
                (383, 251),
                (412, 322),
                (481, 294),
                (398, 237)
)
        if self.map == self.map3:
            pointList = (
                (258, 295),
                (383, 251),
                (412, 364),
                (481, 294),
                (478, 237),
                (383, 251),
                (125, 322),
                (481, 125),
                (398, 237)
)
            
        if self.map == self.map4:
            pointList = (
                (493, 295),
                (292, 251),
                (412, 322),
                (481, 385),
                (398, 237),
                (383, 251),
                (214, 322),
                (481, 195),
                (398, 237)
)
                
        
        self.path = Path(self.enemy, pointList, 2)
        self.path.rotate = False
        self.path.threshold = 5
        
        self.attack = Attack(self)
        
       
        self.villTxt = VillTxt(self)
        
        self.credits1 = Credits1()
        
        self.player = Player(self)
        self.lblOutput = LblOutput()
        
        self.sprites = [self.tileset, self.player,self.lblHealth, self.enemy, self.villTxt]
        
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
        self.map2B = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,1,9,9,9,9],
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
            [12,0,2,0,14,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,11],  
            [12,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11],
            [12,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],  
            [12,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]
        self.map3B = [
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
            [12,2,2,2,1,1,17,1,1,1,1,1,1,2,2,2,2,2,2,11],
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
            [9,9,9,9,9,9,9,6,9,9,9,9,9,9,9,9,9,9,9,9],
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
            [12,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,11],
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
        self.caveRoomB = [
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
        self.endGame = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [12,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,11],
            [12,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,11],
            [12,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,2,11],
            [12,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,11],
            [12,2,1,2,1,2,2,2,2,2,2,2,2,1,2,1,2,1,2,11],
            [12,2,1,2,1,2,15,1,1,1,1,1,1,1,2,1,2,1,2,11],
            [12,2,1,2,1,2,2,2,2,2,2,2,2,2,2,1,2,1,2,11],
            [12,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,11],
            [12,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,11],
            [12,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,11],
            [12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,11],
            [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,4]
]
        self.credits = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
            [12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11],
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
            self.player.position = position
            if self.player.getBomb:
                self.map = self.map3B
                self.player.position = (300, 35)
            else:
                self.map = self.map3
                self.player.position = (300, 35)
                
        #BottomL to TopL if Bomb
        elif self.player.tileOver == (0,9) and self.map == self.map3B:
            position = self.player.position
            self.player.position = position
            self.map = self.map1
            self.player.position = (300, 420)
        
            
#Exit cave if got fish
        elif self.player.tileOver == (4,19) and self.map == self.caveRoomB:
            position = self.player.position
            self.player.position = position
            self.map = self.cave
            self.player.position = (45, 145)            
            
#        BottomL to TopL    
        elif self.player.tileOver == (0,9) and self.map == self.map3:
            position = self.player.position
            self.player.position = position
            self.map = self.map1
            self.player.position = (300, 420)
            
        #TopL to TopR    
        elif self.player.tileOver == (9,19) and self.map == self.map1:
            position = self.player.position
            self.player.position = position
            self.map = self.map2
            self.player.position = (35,300)
            
        #TopR to TopL    
        elif self.player.tileOver == (9,0) and self.map == self.map2:
            position = self.player.position
            self.player.position = position
            self.map = self.map1
            self.player.position = (590, 300)
            
        #BottomL to Bottom R    
        elif self.player.tileOver == (4,19) and self.map == self.map3:
            position = self.player.position
            self.player.position = position
            self.map = self.map4
            self.player.position = (35, 145)
            
        #BottomR to BottomL with bombs
        elif self.player.tileOver == (4,0) and self.map == self.map4:
            position = self.player.position
            self.player.position = position
            if self.player.getBomb:
                self.map = self.map3B
                self.player.position = (590, 145)
            else:
                self.map = self.map3
                self.player.position = (590, 145)
                
        #BottomL to Bottom R with bombs
        elif self.player.tileOver == (4,19) and self.map == self.map3B:
            position = self.player.position
            self.player.position = position
            self.map = self.map4
            self.player.position = (35, 145)            

        
        #BottomR to BottomL
        elif self.player.tileOver == (4,0) and self.map == self.map4:
            position = self.player.position
            self.player.position = position
            self.map = self.map3
            self.player.position = (590, 145)
            
        #BottomR to TopR
        elif self.player.tileOver == (0,10) and self.map == self.map4:
            position = self.player.position
            self.player.position = position
            self.map = self.map2
            self.player.position = (330, 420)
            
        #TopR to BottomR
        elif self.player.tileOver == (14,10) and self.map == self.map2:
            position = self.player.position
            self.player.position = position
            self.map = self.map4
            self.player.position = (330, 35)
            
        #Village
        elif self.player.tileOver == (1,2) and self.map == self.map1:
            position = self.player.position
            self.player.position = position
            self.map = self.village
            self.player.position = (250, 155)
            if self.player.getFish:
                self.villTxt.setImage("VillTxtAfterFish.png")
            else:
                self.villTxt.setImage("VillTxt.png")
            
            
        #Exit Village
        elif self.player.tileOver == (0,9) and self.map == self.village:
            position = self.player.position
            self.player.position = position
            self.map = self.map1
            self.player.position = (80, 75)
            self.villTxt.setImage("VillTxtBlank.png")
            
        #Cave
        elif self.player.tileOver == (9,16) and self.map == self.map4:
            position = self.player.position
            self.player.position = position
            self.map = self.cave
            self.player.position = (80, 75)
        
        #Exit Cave
        elif self.player.tileOver == (0,7) and self.map == self.cave:
            position = self.player.position
            self.player.position = position
            self.map = self.map4
            self.player.position = (475, 300)
            
        #Cave Room
        elif self.player.tileOver == (4,0) and self.map == self.cave:
            position = self.player.position
            self.player.position = position
            if self.player.getFish:
                self.map = self.caveRoomB
                self.player.position = (595, 145)
            else:
                self.map = self.caveRoom
                self.player.position = (595, 145)
    
            
        #Exit Cave Room
        elif self.player.tileOver == (4,19) and self.map == self.caveRoom:
            position = self.player.position
            self.player.position = position
            self.map = self.cave
            self.player.position = (45, 145)
            
        #Exit cave if got fish
        elif self.player.tileOver == (4,19) and self.map == self.caveRoomB:
            position = self.player.position
            self.player.position = position
            self.map = self.cave
            self.player.position = (45, 145)
            
        #Get Fish    
        elif self.player.tileOver == (5,7) and self.map == self.caveRoom:
            position = self.player.position
            self.player.position = position
            self.map = self.caveRoomB
            self.player.tileOver = (5, 7)
            self.player.getFish = True


        #Get QuigBomb    
        elif self.player.tileOver == (9,4) and self.map == self.map3:
            position = self.player.position
            self.player.position = position
            self.map = self.map3B
            self.player.tileOver = (9, 4)
            self.player.getBomb = True
            
        #After Bomb End game    
        elif self.player.tileOver == (1,15) and self.map == self.map2:
            if self.player.getBomb:
                position = self.player.position
                self.player.position = position
                self.map = self.map2B
                self.player.tileOver = (14,8)
            else:
                position = self.player.position
                self.player.position = position
                self.map = self.map2
                self.player.tileOver = (14,17)
        #To end game        
        elif self.player.tileOver == (0,14) or self.player.tileOver == (0,15) and self.map == self.map2B:
            position = self.player.position
            self.player.position = position
            self.map = self.endGame
            self.player.position = (75,75)
            self.player.getFish = False
    
        #Roll Credits
        elif self.player.tileOver == (8,7) and self.map == self.endGame:
            position = self.player.position
            self.player.position = position
            self.map = self.credits
            self.player.position = (400,75)

            credits1 = Credits1()
            credits1.start()
        #Water way to Map 3 
        elif self.player.tileOver == (13,0) and self.map == self.map4 or self.player.tileOver == (14,0) and self.map == self.map4:
            if self.player.getBomb:
                position = self.player.position
                self.player.position = position
                self.map = self.map3B
                self.player.position = (575,400)
            else:
                position = self.player.position
                self.player.position = position
                self.map = self.map3
                self.player.position = (575,400)
                
        #Water way to Map 4
        elif self.player.tileOver == (13,19) and self.map == self.map3 or self.player.tileOver == (13,19) and self.map == self.map3:
            position = self.player.position
            self.player.position = position
            self.map = self.map4
            self.player.position = (50,400)

        
        self.path.process()
        
        self.showMap()
        
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Olympic.jpg")
        self.response = "Quit"
        
        self.player = Player(self)
        
        self.directions = simpleGE.MultiLabel()
        self.fgColor = "None"
        self.bgColor = "None"
        self.directions.textLines = [
        "Welcome to the World of Olympia",
        "A Forgotten Dangerous Land",
        "Can You Bring Back Balance?!",
        "Only Time Will Tell.",
        "Good Luck Traveler"]
        
        self.directions.center = (320, 240)
        self.directions.size = (500,250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnInstructions = simpleGE.Button()
        self.btnInstructions.text = "Instructions"
        self.btnInstructions.center = (320,400)
        
        self.btnMainMenu = simpleGE.Button()
        self.btnMainMenu.text = "Main Menu"
        self.btnMainMenu.center = (700,800)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
             
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.btnInstructions,
                        self.btnMainMenu
                        ]
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnInstructions.clicked:
            self.response = "Instructions"
            self.directions.textLines = [
            "To Move Right, Left, Up, Down",
            "Use the Arrow Keys",
            "",
            "To Attack Press the Space Bar",
            "While Not Moving and Then Move"]
            self.btnMainMenu.center = (320,400)
            self.btnInstructions.center = (700,800)
#             self.btnInstructions == self.btnMainMenu
#             
        if self.btnMainMenu.clicked:
            self.response = "Main Menu"
            self.directions.textLines = [
            "Welcome to the World of Olympia",
            "A Forgotten Dangerous Land",
            "Can You Bring Back Balance?!",
            "Only Time Will Tell.",
            "Good Luck Traveler"]
            self.btnMainMenu.center = (700,800)
            self.btnInstructions.center = (320,400)
            
        if self.player.getBomb:
            self.directions.textLines = [
                "You Win!!"]
            
#             self.btnMainMenu == self.btnInstructions
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
            
def main():
    
    keepGoing = True
    while keepGoing:
        
        instructions = Instructions()
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
        else:
            keepGoing = False
    
    
if __name__ == "__main__":
    main()
    