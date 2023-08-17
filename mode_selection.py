import pygame
import os
import random
import string

# create ID

def generate_random_id(length=20):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

generate_random_id()










# must be generic to be applicable for any games. Player attributes are uploaded online

class player:
    def __init__(self,username,id = None):
        
        # generic details
        #serves as the Player ID
        self.name = username
        self.online = False
        self.checkpoint = None
        
        # Id logic
        self.id = id
        if self.id == None:
            self.id = generate_random_id()
        
        
        # Init nested class
        self.candy_crush = self.candy_crush()
        self.boss_fight = self.boss_fight()
    
    
    
    
    
    
    
    
    # nested Classes 
    
    class candy_crush:
        def __init__(self):
            self.x = None
            self.y = None
            self.width = None
            self.height = None
            self.image = None
            self.rect = None
    class boss_fight:
        def __init__(self):
            self.x = None
            self.y = None
            self.width = None
            self.height = None
            self.image = None
            self.rect = None
    
    
    
    
    
    
    # Funcs

    
    # Gets User ID
    def get_id(self):
        return self.id
    
    
    
    
    
    
    

jack = player("jack")





print(jack.boss_fight.x)
