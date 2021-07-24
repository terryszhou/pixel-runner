import pygame  # <-- import pygame 
from sys import exit # <-- module that closes code once called

pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800, 400)) # <-- declare screen variable, set width & heigth 
pygame.display.set_caption("Terry's Game of Life") # <-- changes window title
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# test_surface = pygame.Surface((200,200)) # <-- solid color test screen
# test_surface.fill("red")

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")

text_surface = test_font.render("My Game", False, "Black") # <-- renders font with text, anti-aliasing Boolean, and color

snail_surface = pygame.image.load("graphics/snail/snail1.png")

while True: # <-- runs forever, renders game, until player input sets False
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50)) # <-- block image transfer: places surface on screen

    pygame.display.update() # <-- update the screen display
    clock.tick(30) # <-- sets while loop to cycle <x> times per second