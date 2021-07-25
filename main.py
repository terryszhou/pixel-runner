# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame  # <-- import pygame 
from sys import exit # <-- module that closes code once called
from random import randint, choice

# # CLASSES - - - - - - - - - - - - - - - - -
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha() # <-- interactable objects always require both a surface and rectangle, or a sprite
        player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha() 
        self.player_walk = (player_walk_1, player_walk_2)
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("audio/audio_jump.mp3")
        self.jump_sound.set_volume(0.05)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load("graphics/Fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/Fly/fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

# # SCORE & COLLISION FUNCTIONS - - - - - - - - - - - - - - - - - - -
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False): # <-- spritecollide(sprite, group, Boolean if group is destroyed)
        obstacle_group.empty()
        return False
    else:
        return True

# # SETUP BASIC VARIABLES - - - - - - - - - - - - - - - - - - -
pygame.init() # <-- initialize pygame 
screen = pygame.display.set_mode((800,400)) # <-- declare screen variable, set width & heigth 
pygame.display.set_caption("Terry's Game of Life") # <-- changes window title
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.05)
bg_music.play(loops = -1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# # SURFACES & RECTANGLES - - - - - - - - - - - - - - - - - - -
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

# INTRO SCREEN - - - - - - - - - - - - - - - - - - -
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2) # <-- rotozoom(variable to be zoomed, angle, scale)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render("Pixel Runner", False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press SPACE to run", False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400, 330))

# ANIMATION TIMERS
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) # <-- set_timer(timer variable, interval in milliseconds)

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
                    # if player_rect.bottom == 300:
                        player_gravity = -20
                else: 
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail"])))

    # # RENDER GAME IF GAME_ACTIVE = TRUE - - - - - - - - - - - - - - - - - - -
    if game_active:
        # # POST-EVENT RENDERING - - - - - - - - - - - - - - - - - - -        
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

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
        # snail_animation_timer = pygame.USEREVENT + 2
        # pygame.time.set_timer(snail_animation_timer, 500)

        # fly_animation_timer = pygame.USEREVENT + 3
        # pygame.time.set_timer(fly_animation_timer, 200)
        # # OBSTACLES - - - - - - - - - - - - - - - - - -
        # # SNAIL - - - - - - - - - - - - - - - - - -
        # snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
        # snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
        # snail_frames = [snail_frame_1, snail_frame_2]
        # snail_frame_index = 0
        # snail_surf = snail_frames[snail_frame_index]

        # # FLY - - - - - - - - - - - - - - - - - -
        # fly_frame_1 = pygame.image.load("graphics/Fly/fly1.png").convert_alpha()
        # fly_frame_2 = pygame.image.load("graphics/Fly/fly2.png").convert_alpha()
        # fly_frames = [fly_frame_1, fly_frame_2]
        # fly_frame_index = 0
        # fly_surf = fly_frames[fly_frame_index]

        # obstacle_rect_list = []

        # # PLAYER 
        # player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha() # <-- interactable objects always require both a surface and rectangle, or a sprite
        # player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha() 
        # player_walk = (player_walk_1, player_walk_2)
        # player_index = 0
        # player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        # player_surf = player_walk[player_index]
        # player_rect = player_surf.get_rect(midbottom = (80,300)) # <-- creates rectangle around a given surface beginning from a given origin
        # player_gravity = 0

        # if event.type == snail_animation_timer:
        #     if snail_frame_index == 0: 
        #         snail_frame_index = 1
        #     else:
        #         snail_frame_index = 0
        #     snail_surf = snail_frames[snail_frame_index]
        # if event.type == fly_animation_timer:
        #     if fly_frame_index == 0:
        #         fly_frame_index = 1
        #     else: 
        #         fly_frame_index = 0
        #     fly_surf = fly_frames[fly_frame_index]

        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80,300)

        # # OBSTACLE FUNCTION
        # def obstacle_movement(obstacle_list):
        #     if obstacle_list:
        #         for obstacle_rect in obstacle_list:
        #             obstacle_rect.x -= 5
        #             if obstacle_rect.bottom == 300:
        #                 screen.blit(snail_surf, obstacle_rect)
        #             else:
        #                 screen.blit(fly_surf, obstacle_rect)
        #         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        #         return obstacle_list
        #     else:
        #         return []

        # def collisions(player, obstacles):
        #     if obstacles:
        #         for obstacle_rect in obstacles:
        #             if player.colliderect(obstacle_rect):
        #                 return False
        #     return True

        # def player_animation():
        #     global player_surf, player_index

        #     if player_rect.bottom < 300:
        #         player_surf = player_jump
        #     else:
        #         player_index += 0.1
        #         if player_index >= len(player_walk):
        #             player_index = 0
        # player_surf = player_walk[int(player_index)]
        # # OBSTACLE MOVEMENT/COLLISION - - - - - - - - - - - - - - - - -
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        # game_active = collisions(player_rect, obstacle_rect_list)


        # # PLAYER MOVEMENT - - - - - - - - - - - - - - - - - - -
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >=300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surf, player_rect)

        # if randint(0,2):
        #     obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300))) # <-- randint(min int, max int)
        # else:
        #     obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

        # snail_rect = snail_surf.get_rect(midbottom = (600,300))

        # # SNAIL MOVEMENT - - - - - - - - - - - - - - - - - - -
        # snail_rect.left -= 6
        # if snail_rect.left < -100:
        #     snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)

        # # SNAIL COLLISION DETECTION - - - - - - - - - - - - - - - - - - -
        # if snail_rect.colliderect(player_rect):
        #     game_active = False
    
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