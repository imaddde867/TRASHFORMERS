import pygame
import sys     # sys-module will be needed to exit the game
from pygame.locals import * # imports the constants of pygame
from pygame.math import Vector2
pygame.init()  # initializes pygame

# add the background music
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)

# the display surface
#both fullscreen option and windowed mode below
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Trashformers")
clock = pygame.time.Clock()
dt = 0

#placeholders for other stuff (animations will be done differently frame by frame)
player = pygame.image.load("character//run_down_2.png").convert_alpha()

#character movement animation
left = False
right = False
up = False
down = False
moveCount = 0 
#movements anim as lists to loop through
moveRight = [pygame.image.load("character//run_right_1.png").convert_alpha(), pygame.image.load("character//run_right_2.png").convert_alpha(), pygame.image.load("character//run_right_3.png").convert_alpha()]
moveLeft = [pygame.image.load("character//run_left_1.png").convert_alpha(), pygame.image.load("character//run_left_2.png").convert_alpha(), pygame.image.load("character//run_left_3.png").convert_alpha()]
moveUp = [pygame.image.load("character//run_up_1.png").convert_alpha(), pygame.image.load("character//run_up_2.png").convert_alpha(), pygame.image.load("character//run_up_3.png").convert_alpha()]
moveDown = [pygame.image.load("character//run_down_1.png").convert_alpha(), pygame.image.load("character//run_down_2.png").convert_alpha(), pygame.image.load("character//run_down_3.png").convert_alpha()]

#trash = pygame.image.load("trash.png").convert()
level = pygame.image.load("level.png").convert()
#trash cans
plastic = pygame.image.load("bins//plastic.png").convert_alpha()
metal = pygame.image.load("bins//metal.png").convert_alpha()
glass = pygame.image.load("bins//glass.png").convert_alpha()
paper = pygame.image.load("bins//paper.png").convert_alpha()
organic = pygame.image.load("bins//organic.png").convert_alpha()

trash_plastic = [pygame.image.load("trash//plastic_1.png").convert_alpha(), pygame.image.load("trash//plastic_2.png").convert_alpha(), pygame.image.load("trash//plastic_3.png").convert_alpha(), pygame.image.load("trash//plastic_4.png").convert_alpha(), pygame.image.load("trash//plastic_5.png").convert_alpha(), pygame.image.load("trash//plastic_6.png").convert_alpha(), pygame.image.load("trash//plastic_7.png").convert_alpha()]
trash_metal = [pygame.image.load("trash//metal_1.png").convert_alpha(), pygame.image.load("trash//metal_2.png").convert_alpha(), pygame.image.load("trash//metal_3.png").convert_alpha(), pygame.image.load("trash//metal_4.png").convert_alpha(), pygame.image.load("trash//metal_5.png").convert_alpha(), pygame.image.load("trash//metal_6.png").convert_alpha(), pygame.image.load("trash//metal_7.png").convert_alpha()]
trash_glass = [pygame.image.load("trash//glass_1.png").convert_alpha(), pygame.image.load("trash//glass_2.png").convert_alpha(), pygame.image.load("trash//glass_3.png").convert_alpha(), pygame.image.load("trash//glass_4.png").convert_alpha(), pygame.image.load("trash//glass_5.png").convert_alpha(), pygame.image.load("trash//glass_6.png").convert_alpha(), pygame.image.load("trash//glass_7.png").convert_alpha()]
trash_paper = [pygame.image.load("trash//paper_1.png").convert_alpha(), pygame.image.load("trash//paper_2.png").convert_alpha(), pygame.image.load("trash//paper_3.png").convert_alpha(), pygame.image.load("trash//paper_4.png").convert_alpha(), pygame.image.load("trash//paper_5.png").convert_alpha(), pygame.image.load("trash//paper_6.png").convert_alpha(), pygame.image.load("trash//paper_7.png").convert_alpha()]
trash_organic = [pygame.image.load("trash//organic_1.png").convert_alpha(), pygame.image.load("trash//organic_2.png").convert_alpha(), pygame.image.load("trash//organic_3.png").convert_alpha(), pygame.image.load("trash//organic_4.png").convert_alpha(), pygame.image.load("trash//organic_5.png").convert_alpha(), pygame.image.load("trash//organic_6.png").convert_alpha(), pygame.image.load("trash//organic_7.png").convert_alpha()]


#player start position
player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)

#trash can positions (sprites and stuff might be less code intensive)
plastic_pos = pygame.Vector2(screen.get_width() / 2 - 205, screen.get_height() / 2 - 275)
metal_pos = pygame.Vector2(screen.get_width() / 2 - 120, screen.get_height() / 2 - 275)
glass_pos = pygame.Vector2(screen.get_width() / 2 - 40, screen.get_height() / 2 - 275)
paper_pos = pygame.Vector2(screen.get_width() / 2 + 40, screen.get_height() / 2 - 275)
organic_pos = pygame.Vector2(screen.get_width() / 2 + 110, screen.get_height() / 2 - 275)


# pygame.image.load(file) function loads a picture "file" into a given variable
# convert() method converts the picture into the right pixel-format
# picture files needs to be in the same folder as this python file
# the folder path can be relative or absolute:
# relative path: mario = pygame.image.load("folder//mario.png").convert()
# absolute path: fireball = pygame.image.load("C://folder//fireball.png").convert()


# RGB-colors are tuples (r,g,b), where 0<r,g,b<255
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,0,130)

# Surface objects can be filled with a color using fill() method
# Surface objects can be added to the display surface with blit() method
# blit(Surface,(x,y)) adds "Surface" into coordinates (x,y)=(left, top)
#screen.blit(level, (0,0))



# the display surface needs to be updated for the blitted Surfaces to become visible
# pygame.display.update() would do the same
#pygame.display.flip()

# Surface.get_rect() method returns the Rect object of "Surface"
# Rect objects are needed to move Surfaces and for collision detection
# Rect(left, top, width, height) contains left/top-coordinates and width/height
playerArea = player.get_rect(center = player_pos) #we set the players rects center to be player_pos
plasticArea = plastic.get_rect(center = plastic_pos)
metalArea = metal.get_rect(center = metal_pos)
glassArea = glass.get_rect(center = glass_pos)
paperArea = paper.get_rect(center = paper_pos)
organicArea = organic.get_rect(center = organic_pos)

# get_rect() method by default sets the left-top corner to (0,0)
# player and rectangle were not blitted into (0,0)
# the left and top coordinates have to be changed with dot notation
#playerArea.left = 400
#playerArea.top = 500


#setting the default value for moving the player(this can be used to interrupt movement when colliding)
moving_player = False

#gets the mouse position
prev_mouse_pos = Vector2(pygame.mouse.get_pos())

# the game loop which runs until sys.exit()
while True:


    
    # loop to check if the user has closed the display window or pressed esc
    for event in pygame.event.get():  # list of all the events in the event queue
        if event.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display window closes
            sys.exit()    # the python program exits
        if event.type == KEYDOWN:     # if the player pressed down any key
            if event.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display window closes
                sys.exit()    # the python program exits
        #makes the player move
        elif event.type == MOUSEBUTTONDOWN:
            if playerArea.collidepoint(event.pos):
                moving_player = True
        #stops movement
        elif event.type == MOUSEBUTTONUP:
            moving_player = False
            pygame.mouse.set_visible(True)

            x,y = pygame.mouse.get_pos()
            print(x, y)

        elif event.type == MOUSEMOTION and moving_player:
            pygame.mouse.set_visible(False)
            playerArea.move_ip(event.rel)
            #x,y = event.pos
            
            #current mouse position
            cur_mouse_pos = Vector2(pygame.mouse.get_pos())
            if cur_mouse_pos.x < prev_mouse_pos.x:
                left = True
                right = False
                up = False
                down = False

            elif cur_mouse_pos.x > prev_mouse_pos.x:
                right = True
                left = False
                up = False
                down = False

            elif cur_mouse_pos.y < prev_mouse_pos.y:
                up = True
                left = False
                right = False
                down = False

            elif cur_mouse_pos.y > prev_mouse_pos.y:
                down = True
                up = False
                left = False
                right = False

            prev_mouse_pos = cur_mouse_pos


    # player can be moved with left/right/up/down-keys
    # get.pressed() function gives a boolean list of all the keys if they are being pressed
    #pressings = pygame.key.get_pressed()
    #if pressings[K_LEFT] and player_pos.x > 310:          # if left-key is true in the list
        #player_pos.x -= 300 * dt  
    #if pressings[K_RIGHT] and player_pos.x < 1585:         # if you hit the texture the effect doesn’t work
        #player_pos.x += 300 * dt
    #if pressings[K_DOWN] and player_pos.y < 798:
        #player_pos.y += 300 * dt
    #if pressings[K_UP] and player_pos.y > 250:
        #player_pos.y -= 300 * dt


    # blit all the Surfaces in their new places
    screen.blit(level, (0,0)) # without this, moving characters would have a "trace"
    screen.blit(metal, metal_pos)
    screen.blit(glass, glass_pos)
    screen.blit(plastic, plastic_pos)
    screen.blit(paper, paper_pos)
    screen.blit(organic, organic_pos)

    if moveCount + 1 >= 12: #3 images per move anim and all shown for 4 frames => upper limit = 12
        moveCount = 0
    if left and moving_player:
        screen.blit(moveLeft[moveCount//4], playerArea) #1 image shown for 4 frames
        moveCount += 1
    elif right and moving_player:
        screen.blit(moveRight[moveCount//4], playerArea)
        moveCount += 1
    elif up and moving_player:
        screen.blit(moveUp[moveCount//4], playerArea)
        moveCount += 1
    elif down and moving_player:
        screen.blit(moveDown[moveCount//4], playerArea)
        moveCount += 1
    else:
        screen.blit(player, playerArea)
        moveCount = 0

    
    # updating the display surface is always needed at the end of each iteration of game loop
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
