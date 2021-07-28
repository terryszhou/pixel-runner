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