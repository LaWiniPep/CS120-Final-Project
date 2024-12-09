import pygame, simpleGE
from Final_Project_Working import *

class Credits1(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Olympic.jpg")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.fgColor = "None"
        self.bgColor = "None"
        self.directions.textLines = [
        "",
        "YOU WIN!!!",
        "Would you like to return to the land?",
        "We will reset your memories.",
        ""]
        
        self.directions.center = (320, 240)
        self.directions.size = (500,250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Return"
        self.btnPlay.center = (100, 400)
        
        self.btnInstructions = simpleGE.Button()
        self.btnInstructions.text = "Credits"
        self.btnInstructions.center = (320,400)
        
        self.btnMainMenu = simpleGE.Button()
        self.btnMainMenu.text = "Main Menu"
        self.btnMainMenu.center = (700,800)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Escape"
        self.btnQuit.center = (540, 400)
             
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.btnInstructions,
                        self.btnMainMenu
                        ]
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Return"
            instructions = Instructions()
            instructions.start()

            
        if self.btnInstructions.clicked:
            self.response = "Credits"
            self.directions.textLines = [
            "Andrew Harris - Basically Everything",
            "Open Game Art txt file",
            "Universal LPC Spritesheet Genterator",
            "Ball State University",
            "My Wife"]
            self.btnMainMenu.center = (320,400)
            self.btnInstructions.center = (700,800)
#             self.btnInstructions == self.btnMainMenu
#             
        if self.btnMainMenu.clicked:
            self.response = "Main Menu"
            self.directions.textLines = [
            "",
            "YOU WIN!!!",
            "Would you like to return to the land?",
            "We will reset your memories."]
            self.btnMainMenu.center = (700,800)
            self.btnInstructions.center = (320,400)
            
            
        if self.btnQuit.clicked:
            self.response = "Escacpe"
            self.stop()