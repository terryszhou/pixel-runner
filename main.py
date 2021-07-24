import pygame  # <-- import pygame 

pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800,800)) # <-- declare screen variable, set width & heigth 

while True: # <-- runs forever, renders game, until player input sets False
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit() 
    pygame.display.update() # <-- update the screen display