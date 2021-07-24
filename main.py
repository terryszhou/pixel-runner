# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame  # <-- import pygame 
from sys import exit # <-- module that closes code once called

# # SCORE FUNCTION - - - - - - - - - - - - - - - - - - -
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

# # SETUP BASIC VARIABLES - - - - - - - - - - - - - - - - - - -
pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800,400)) # <-- declare screen variable, set width & heigth 
pygame.display.set_caption("Terry's Game of Life") # <-- changes window title
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

# # SURFACES & RECTANGLES - - - - - - - - - - - - - - - - - - -
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha() # <-- interactable objects always require both a surface and rectangle, or a sprite
player_rect = player_surf.get_rect(midbottom = (80,300)) # <-- creates rectangle around a given surface beginning from a given origin
player_gravity = 0

# INTRO SCREEN - - - - - - - - - - - - - - - - - - -
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2) # <-- rotozoom(variable to be zoomed, angle, scale)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render("Pixel Runner", False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press SPACE to run", False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400, 330))

# # GAME LOOP - - - - - - - - - - - - - - - - - - -
while True: # <-- runs forever, renders game, until player input sets False

    # # EVENT HANDLING - - - - - - - - - - - - - - - - - - -
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    if player_rect.bottom == 300:
                        player_gravity = -20
                else: 
                    game_active = True
                    snail_rect.x = 600
                    start_time = int(pygame.time.get_ticks() / 1000)

    # # RENDER GAME IF GAME_ACTIVE = TRUE - - - - - - - - - - - - - - - - - - -
    if game_active:
        # # POST-EVENT RENDERING - - - - - - - - - - - - - - - - - - -
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        score = display_score()

        # # SNAIL MOVEMENT - - - - - - - - - - - - - - - - - - -
        snail_rect.left -= 6
        if snail_rect.left < -100:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # # PLAYER MOVEMENT - - - - - - - - - - - - - - - - - - -
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # # SNAIL COLLISION DETECTION - - - - - - - - - - - - - - - - - - -
        if snail_rect.colliderect(player_rect):
            game_active = False

    # # RENDER GAME-OVER STATE  - - - - - - - - - - - - - - - - - - -
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(f"Your Score: {score}", False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
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

        # # BASIC JUMP ON MOUSE CLICK - - - - - - - - - - - - - - -
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #         player_gravity = -20

        # # SAMPLE SHAPES - - - - - - - - - - - - - - - - -
        # pygame.draw.line(screen, "Gold", (0,0), (800,400), 10) # <-- surface, color, start-point, end-point, width
        # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))

        # # SAMPLE SURFACES
        # test_surface = pygame.Surface((200,200)) # <-- solid color test screen
        # test_surface.fill("red")

        # # SAMPLE SCORE TEXT
        # score_surf = test_font.render("My Game", False, (64,64,64)) # <-- renders font with text, anti-aliasing Boolean, and color
        # score_rect = score_surf.get_rect(center = (400,50))
        # pygame.draw.rect(screen, (195,234,233), score_rect)
        # pygame.draw.rect(screen, (195,234,233), score_rect, 6) # <-- surface, color, which rectangle, width
        # screen.blit(score_surf, score_rect) # <-- block image transfer: places surface on screen