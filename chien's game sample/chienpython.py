
import pygame
import sys, os, random
pygame.init()


# screen proportions
os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()
info = pygame.display.Info() # You have to call this before pygame.display.set_mode()

screen_width,screen_height = info.current_w,info.current_h




WIDTH = screen_width
HEIGHT = screen_height - 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)

# Set the title of the window
pygame.display.set_caption("Candy Crush game")




# non trash
x2 = pygame.image.load("2.png")
x3 = pygame.image.load("3.png")
x4 = pygame.image.load("4.png")
x5 = pygame.image.load("5.png")
x6 = pygame.image.load("6.png")
x7 = pygame.image.load("7.png")
x8 = pygame.image.load("8.png")
x9 = pygame.image.load("9.png")



# trash
x1 = pygame.image.load("1.png")
x10 = pygame.image.load("10.png")
x11 = pygame.image.load("11.png")







# tiles list
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
choices = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11]



# randomize method
for i in range(5):
    row1.append(random.choice(choices))
    row2.append(random.choice(choices))
    row3.append(random.choice(choices))
    row4.append(random.choice(choices))
    row5.append(random.choice(choices))

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)



# Display images
def display_grid():
    for row_num, row in enumerate([row1, row2, row3, row4, row5]):
        for col_num, image in enumerate(row):
            x = col_num * image.get_width()
            y = row_num * image.get_height()
            WIN.blit(image, (x, y))



class Game():
    def __init__(self):
        self.running = True













game = Game()


while game.running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    WIN.fill((255, 255, 255))
    display_grid()
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()