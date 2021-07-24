import pygame  # <-- import pygame 
from sys import exit # <-- module that closes code once called

pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800,400)) # <-- declare screen variable, set width & heigth 
pygame.display.set_caption("Terry's Game of Life") # <-- changes window title
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# test_surface = pygame.Surface((200,200)) # <-- solid color test screen
# test_surface.fill("red")

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

score_surf = test_font.render("My Game", False, (64,64,64)) # <-- renders font with text, anti-aliasing Boolean, and color
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha() # <-- interactable objects always require both a surface and rectangle, or a sprite
player_rect = player_surf.get_rect(midbottom = (80,300)) # <-- creates rectangle around a given surface beginning from a given origin
player_gravity = 0

while True: # <-- runs forever, renders game, until player input sets False
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    pygame.draw.rect(screen, (195,234,233), score_rect)
    pygame.draw.rect(screen, (195,234,233), score_rect, 6) # <-- surface, color, which rectangle, width
    screen.blit(score_surf, score_rect) # <-- block image transfer: places surface on screen

    snail_rect.left -= 4
    if snail_rect.left < -100:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >=300:
        player_rect.bottom = 300
    screen.blit(player_surf, player_rect)

    pygame.display.update() # <-- update the screen display
    clock.tick(60) # <-- sets while loop to cycle <x> times per second

    # # # SCRAP CODE
    # # BASIC KEY DETECTOR - - - - - - - - - - - - - - - - - -
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    # # BASIC COLLISION DETECTOR - - - - - - - - - - - - - - - - - -
    # if player_rect.colliderect(snail_rect): # <-- returns 0 on non-collision, 1 on collision
    #     print("Collision")

    # # BASIC MOUSE COLLISION DETECTOR - - - - - - - - - - - - - - - - - -
    # mouse_pos = pygame.mouse.get_pos() # <-- sets coordinates for mouse cursor position
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed()) # <-- returns False if mouse button not pressed, True if pressed

    # # SAMPLE SHAPES - - - - - - - - - - - - - - - - -
    # pygame.draw.line(screen, "Gold", (0,0), (800,400), 10) # <-- surface, color, start-point, end-point, width
    # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))