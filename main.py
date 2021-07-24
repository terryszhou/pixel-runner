import pygame  # <-- import pygame 
from sys import exit # <-- module that closes code once called

pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800,800)) # <-- declare screen variable, set width & heigth 
pygame.display.set_caption("Terry's Game of Life") # <-- changes window title
clock = pygame.time.Clock()

test_surface = pygame.Surface((200,200))
test_surface.fill("red")

while True: # <-- runs forever, renders game, until player input sets False
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()

    screen.blit(test_surface, (0, 0)) # <-- block image transfer: places surface on screen

    pygame.display.update() # <-- update the screen display
    clock.tick(30) # <-- sets while loop to cycle <x> times per second