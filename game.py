import pygame
import finish_screen
import menu_screen
import boss_fight
import candy_crush
import pyrebase
import settings


# important notes. If calling a class attribute, make sure to not add parenthesis if not a method and also make sure you allocated the class into a vatiable.



class game:
    def __init__(self):
        self.state = "intro"
    def game_manager(self):
        if self.state == "intro":
        
        if self.state   



running = True
while running:
    # game loop