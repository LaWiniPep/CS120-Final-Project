import simpleGE
import pygame

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
        moved = False

        if self.isKeyPressed(pygame.K_LEFT):
            if self.x > 0:
                self.x -= self.speed
            elif self.scene.offCol > 0:
                self.scene.offCol -= 1
                self.x = self.scene.WINDOW_WIDTH - self.width
            else:
                self.scene.switchMap("left")
            moved = True

        if self.isKeyPressed(pygame.K_RIGHT):
            if self.x < self.scene.WINDOW_WIDTH - self.width:
                self.x += self.speed
            elif self.scene.offCol < self.scene.COLS - self.scene.SCREEN_COLS:
                self.scene.offCol += 1
                self.x = 0
            else:
                self.scene.switchMap("right")
            moved = True

        if self.isKeyPressed(pygame.K_UP):
            if self.y > 0:
                self.y -= self.speed
            elif self.scene.offRow > 0:
                self.scene.offRow -= 1
                self.y = self.scene.WINDOW_HEIGHT - self.height
            else:
                self.scene.switchMap("up")
            moved = True

        if self.isKeyPressed(pygame.K_DOWN):
            if self.y < self.scene.WINDOW_HEIGHT - self.height:
                self.y += self.speed
            elif self.scene.offRow < self.scene.ROWS - self.scene.SCREEN_ROWS:
                self.scene.offRow += 1
                self.y = 0
            else:
                self.scene.switchMap("down")
            moved = True

        if moved:
            self.scene.map()
