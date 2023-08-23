import pygame
import finish_screen
import menu_screen
import boss_fight
import candy_crush
import pyrebase
import settings



class candy_crush:
    def __init__(self):
        self.candy_crush = self.candy_crush
        
    class candy:
        pass



# Game logic


class Game:
    def __init__(self):
        self.state = "intro"
        
    def game_manager(self):
        if self.state == "intro":
            print("you are at the intro!")
        elif self.state == "candy_crush":
            print("you are at candy crush!")
        elif self.state == "end_screen":
            print("you are at end screen!")
game = Game() # Create an instance



running = True
while running:
    # game loop
    game.game_manager()
    
    if game.state = 