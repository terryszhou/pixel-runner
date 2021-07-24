import pygame  # <-- import pygame 
from sys import exit # <-- module that closes code once called

pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800, 400)) # <-- declare screen variable, set width & heigth 
pygame.display.set_caption("Terry's Game of Life") # <-- changes window title
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# test_surface = pygame.Surface((200,200)) # <-- solid color test screen
# test_surface.fill("red")

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()
text_surf = test_font.render("My Game", False, "Black") # <-- renders font with text, anti-aliasing Boolean, and color

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha() # <-- interactable objects always require both a surface and rectangle, or a sprite
player_rect = player_surf.get_rect(midbottom = (80, 300)) # <-- creates rectangle around a given surface beginning from a given origin

while True: # <-- runs forever, renders game, until player input sets False
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(text_surf, (300, 50)) # <-- block image transfer: places surface on screen
    snail_rect.left -= 4
    if snail_rect.left < -100:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    pygame.display.update() # <-- update the screen display
    clock.tick(60) # <-- sets while loop to cycle <x> times per second