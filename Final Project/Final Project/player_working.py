import pygame, simpleGE

class LblHealth (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Heart3.png")
        self.setSize(96,16)
        self.position = (100, 16)
        
class Bomb (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("QuiqBomb.png")
        self.setSize(16,16)
        self.position = (288, 96)
        
class Paul (simpleGE.Sprite):
    def __init__(self,scene):
        super().__init(scene)
        self.setImage("Paul.png")
        self.setSize(32,32)
        self.position = (200,150)
        
class Villager (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Villager.png")
        self.setSize(32,32)
        self.position = (300, 150)
        
class VillTxt(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
#         self.center = (320, 25)
        self.setImage("VillTxtBlank.png")
        self.setSize(250,64)
        self.center = (35, 35)
        self.position = (250,250)
        self.fgColor = "none"
        self.bgColor = "none"
        self.clearBack = True           
        
class LblOutput(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 25)
        self.text = "current tile: "
        self.fgColor = "black"
        self.clearBack = True
        
class Attack(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("PlayerAttack.png", (32,32), 4, 5, .1)
        self.tileOver = (0,0)
        self.walkAnim.startCol = 0
        self.animRow = 2
        
class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("PlayerSpriteMove.png", (32,32), 4, 9, .1)
        self.tileOver = (0,0)
        self.walkAnim.startCol = 0
        self.animRow = 2
        self.moveSpeed = 1
        self.playerDir = "N"
        self.attackAnim = simpleGE.SpriteSheet("PlayerAttack.png", (32,32), 4, 5, .1)
        self.isAttacking = False
        self.attackDuration = 0.5
        self.attackStartTime = 0
        self.getFish = False
        self.getBomb = False
        self.getPaul = False
        
    def process(self):
        self.dx = 0
        self.dy = 0
        walking = False
        attack = False
        getFish = False
        getBomb = False
        
        if self.isKeyPressed(pygame.K_UP):
            self.animRow = 0
            self.dy -= self.moveSpeed
            walking = True
            attack = False
            self.playerDir = "N"
            
        if self.isKeyPressed(pygame.K_DOWN):
            self.animRow = 2
            self.dy += self.moveSpeed
            walking = True
            attack = False
            self.playerDir = "S"
            
        if self.isKeyPressed(pygame.K_LEFT):
            self.animRow = 1
            self.dx -= self.moveSpeed
            walking = True
            attack = False
            self.playerDir = "W"
            
        #Attack Right    
        if self.isKeyPressed(pygame.K_RIGHT):
            self.animRow = 3
            self.dx += self.moveSpeed
            walking = True
            attack = False
            self.playerDir = "E"
            
        if self.isKeyPressed(pygame.K_SPACE) and self.playerDir == "N":
            self.isAttacking = True
            self.attackStartTime = pygame.time.get_ticks()
            self.animRow = 0


        elif self.isKeyPressed(pygame.K_SPACE) and self.playerDir == "S":
            self.isAttacking = True
            self.attackStartTime = pygame.time.get_ticks()
            self.animRow = 1
            self.getFish = True
            
        elif self.isKeyPressed(pygame.K_SPACE) and self.playerDir == "E":
            self.isAttacking = True
            self.attackStartTime = pygame.time.get_ticks()
            self.animRow = 3
            
        elif self.isKeyPressed(pygame.K_SPACE) and self.playerDir == "W":
            self.isAttacking = True
            self.attackStartTime = pygame.time.get_ticks()
            self.animRow = 2 
            self.getbomb = True
            
        #Stop attack animation
        currentTime = pygame.time.get_ticks()
        if self.isAttacking and currentTime - self.attackStartTime > self.attackDuration *1000:
            self.isAttacking = False
            self.walkAnim = simpleGE.SpriteSheet("PlayerSpriteMove.png", (32,32), 4, 9, .1)
        #Walking    
        if walking:
            self.copyImage(self.walkAnim.getNext(self.animRow))
        elif self.isAttacking:
            self.walkAnim = simpleGE.SpriteSheet("PlayerAttack.png", (32,32), 4, 5, .1)
            self.copyImage(self.walkAnim.getNext(self.animRow))

        else:
            self.copyImage(self.walkAnim.getCellImage(0, self.animRow))
            
            
        
        #Speed on different tiles
        if self.tileState == 0:
            self.moveSpeed = 1
        elif self.tileState == 1:
            self.moveSpeed = 2
        elif self.tileState == 2:
            if self.getFish == True:
                self.moveSpeed = .1
            else:
                self.moveSpeed = 2
        elif self.tileState == 9:
            self.y += 2
        elif self.tileState == 10:
            self.y -= 2
        elif self.tileState == 11:
            self.x -= 2
        elif self.tileState == 12:
            self.x += 2
        
        else:
            self.moveSpeed = 2
        

