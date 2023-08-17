import pygame
import finish_screen
import menu_screen
import boss_fight
import candy_crush
import pyrebase
import settings



'''
The main game loop, Here is where the game loop is executed.

'''




# where elements gets blit and draw
def draw_window():
    pass



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    
    
    
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()

