self.map1 = [
            
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],  
            [4,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
            [4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4],  
            [4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4],  
            [4,0,2,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],  
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

def loadMap1(self):
        
        self.currentMapData = [
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [4,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,4],
            [4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4]
]
        for row in range(self.SCREEN_ROWS):
            self.tileset.append([])
            for col in range(self.SCREEN_COLS):
                currentMap = self.map1
                currentVal = currentMap[row][col]
                newTile = Tile(self)
                newTile.setState(currentVal)
                newTile.tilePos = (row,col)
                xPos = 16 + (32 * col)
                yPos = 16 + (32 * row)
                newTile.x = xPos
                newTile.y = yPos
                self.tileset[row].append(newTile)

            self.showMap()

    def loadMap2(self):
        self.currentMapData = [
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,4],
            [4,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,4],
            [4,4,4,4,4,4,4,4,4,1,1,4,4,4,4,4,4,4,4,4]
]
        
    def loadMap3(self):

        self.currentMapData = [
            [4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4],  
            [4,0,2,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,4],  
            [4,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,4],  
            [4,0,2,2,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1],  
            [4,0,2,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1],
            [4,0,2,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,4],  
            [4,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
            [4,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],  
            [4,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
]
        
    def loadMap4(self):
        
self.village = [
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,4],
            [2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
]
    