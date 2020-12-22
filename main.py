import pygame
import math
import random
from pygame import mixer  # it is atlas that help us to handle all kinds of music inside the game

# initialising the pygame (always)
pygame.init()




# create the surface (i.e., screen) (width, height)
surface = pygame.display.set_mode((900, 600))

# Changing title and game_icon
pygame.display.set_caption('Ghost Shooting')
game_icon = pygame.image.load('Aircraft 24 pxl.png')
pygame.display.set_icon(game_icon)

# Loading the background image
background_img = pygame.image.load('background image.jpg')

# loading and playing the background sound
mixer.music.load('background sound.mp3')  # music - used to play the sound continuously (used for long sound)
mixer.music.play(-1)  # to play the music again and again (looping)




# adding aircraft image and setting x and y co-ordinates
aircraft_img = pygame.image.load('aircraft.png')
aircraft_X = 420
aircraft_Y = 520
aircraft_X_change = 0

# adding ghost image and setting x and y co-ordinates
ghost_img = []
ghost_X = []
ghost_Y = []
ghost_X_change = []
ghost_Y_change = []
no_of_ghosts = 10

for i in range(no_of_ghosts ):
    ghost_img.append(pygame.image.load('red ghost.png'))
    ghost_X.append(random.randint(0, 836))
    ghost_Y.append(random.randint(0, 150))
    ghost_X_change.append(0.7)                               # change of ghost_X_change pxls per while loop
    ghost_Y_change.append(50)                                # change of ghost_Y_change pxls every time

# adding missile image and setting x and y co-ordinates
# load - missile can't be seen on surface
# launch - missile is currently moving
missile_img = pygame.image.load('missile.png')
missile_X = 0
missile_Y = 520
missile_X_change = 0
missile_Y_change = 12
missile_state = 'load'





# Selecting font and it's size to display 'score'
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 25)     # (font name, size)
text_X = 10      # pxl distance where score has to be shown
text_Y = 10

# Selecting font and it's size to display 'Game Over' and 'Final Score'
game_over_font = pygame.font.Font('freesansbold.ttf', 65 )
final_score_font = pygame.font.Font('freesansbold.ttf', 50 )

# Selecting font and it's size to display Name of game, 'Pause' and functions of keys to play the game
common_font = pygame.font.Font('freesansbold.ttf', 65)
key_functions_font = pygame.font.Font('freesansbold.ttf', 30)




# blit = draw -> to draw image of aircraft on surface
def draw_aircraft(x, y):
    surface.blit(aircraft_img , (x, y))

# blit = draw -> to draw image of ghost on surface
def draw_ghost(x, y, i):
    surface.blit(ghost_img[i], (x, y))

# function to launch the missile from the aircraft
def launch_missile(x, y):
    global missile_state
    missile_state = 'launch'
    surface.blit(missile_img, (x + 20, y))

# function to show the score
def show_score(x, y):
    score = score_font.render('SCORE: ' + str(score_value), True, (0, 0, 0))
    surface.blit(score, (x, y))



# function to check the collision between missile and ghost
def check_collision(ghost_X, ghost_Y, missile_X, missile_Y):
    D = math.sqrt(pow(ghost_X - missile_X, 2) + pow(ghost_Y - missile_Y, 2))
    if D < 35:
        return True



# function to pause/resume the game and to display functions of the keys
def pause_resume() :
    is_paused = True
    while is_paused :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p :
                    is_paused = False
                if event.key == pygame.K_q :
                    quit()
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()
        surface.fill((0, 200, 0))

        display_pause = common_font.render('PAUSED', True, (0, 0, 0))
        surface.blit(display_pause, (325, 50))

        display_key_functions1 = key_functions_font.render('Press left arrow key/a to move the aircraft left. ', True,(0, 0, 0))
        surface.blit(display_key_functions1, (10, 200))

        display_key_functions2 = key_functions_font.render('Press right arrow key/d to move the aircraft right. ', True,(0, 0, 0))
        surface.blit(display_key_functions2, (10, 250))

        display_key_functions3 = key_functions_font.render('Press space to launch missile.', True, (0, 0, 0))
        surface.blit(display_key_functions3, (10, 300))

        display_key_functions4 = key_functions_font.render('Press P to pause and resume.', True, (0, 0, 0))
        surface.blit(display_key_functions4, (10, 350))

        display_key_functions5 = key_functions_font.render('Press Q or cross to quit.', True, (0, 0, 0))
        surface.blit(display_key_functions5, (10, 400))

# function to print 'Game Over' and 'Final Score'
def game_over_text():
    text_game_over = game_over_font.render('GAME OVER!', True, (0, 0, 0))
    surface.blit(text_game_over, (225, 200))
    text_final_score = final_score_font.render('FINAL SCORE: ' + str(score_value), True, (0, 0, 0))
    surface.blit(text_final_score, (230, 270))

# function to display completion of level
def level_complete() :
    is_paused = True
    while is_paused :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p :
                    is_paused = False
                if event.key == pygame.K_q :
                    quit()
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()
        surface.fill((0, 200, 0))

        display_level_complete = common_font.render('Level Completed', True, (0, 0, 0))
        surface.blit(display_level_complete, (150, 200))






# Starting - displaying name of game and some functions of the keys
not_started = True
while not_started :
    pygame.display.update()
    surface.fill((255, 128, 0))

    game_name = common_font.render('GHOST SHOOTING', True, (0, 0, 0))
    surface.blit(game_name, (150, 50))

    display_action1 = key_functions_font.render('Press S to start.', True,(0, 0, 0))
    surface.blit(display_action1, (10, 150))

    display_action2 = key_functions_font.render('Press P to pause/resume and for functions of the keys used.', True,(0, 0, 0))
    surface.blit(display_action2, (10, 200))

    display_action3 = key_functions_font.render('Press Q or cross to quit.', True,(0, 0, 0))
    surface.blit(display_action3, (10, 250))


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s :
                not_started = False
            if event.type == pygame.QUIT or event.key == pygame.K_q:
                quit()
        if event.type == pygame.QUIT :
            quit()


# Game loop so to keep game window open till the close button(cross button) is not pressed
carry_on = True
while carry_on:                         # the operations which to be always on surface (display screen) should be under while loop
    pygame.display.update()             # (always) - since objects will move on surface (screen) so it should always be updating

    surface.blit(background_img, (0, 0))
    draw_aircraft(aircraft_X,aircraft_Y)    # calling the function inside while - to always show the aircraft, always after background image - so that aircraft should be above te surface
    show_score(text_X, text_Y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False

        # to check if any key is pressed and which key - (left or right arrow key, space bar) - is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                aircraft_X_change = -2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                aircraft_X_change = 2
            if event.key == pygame.K_SPACE :
                if missile_state == 'load':  # missile will be launched only if missile_state is 'load'
                    missile_sound = mixer.Sound('silent-gun.wav')  # used sound to play the sound for short duration
                    missile_sound.play()
                    missile_X = aircraft_X
                    launch_missile(missile_X, missile_Y)
            if event.key == pygame.K_p :
                pause_resume()
            if event.key == pygame.K_q:
                quit()

        if event.type == pygame.KEYUP:                  # to stop the motion of aircraft on lifting the 'left or right arrow key' up
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d :
                aircraft_X_change = 0



    aircraft_X += aircraft_X_change

    # creating the boundries
    if aircraft_X < 0:
        aircraft_X = 0
    elif aircraft_X > 836:
        aircraft_X = 836



    for i in range(no_of_ghosts):


        # motion of ghost
        ghost_X[i] += ghost_X_change[i]  # ghost_X is changing continuously , not ghost_Y
        if ghost_X[i] < 0:
            ghost_X_change[i] = 0.7
            ghost_Y[i] += ghost_Y_change[i]

        elif ghost_X[i] > 836:
            ghost_X_change[i] = -0.7
            ghost_Y[i] += ghost_Y_change[i]

        # if collision between missile and ghost occurs then missile does not pass the ghost and score increases
        collision = check_collision(ghost_X[i], ghost_Y[i], missile_X, missile_Y)
        if collision:
            exposion_Sound = mixer.Sound('explosion sound.wav')  # used sound to play the sound for short duration
            exposion_Sound.play()
            missile_state = 'load'
            missile_Y = 520
            score_value += 10
            ghost_X[i] = random.randint(0, 836)
            ghost_Y[i] = random.randint(0, 150)
        draw_ghost(ghost_X[i], ghost_Y[i], i)

        # If the any ghost crosses the line then 'Game over'
        if ghost_Y[i] > 450:
            for j in range(no_of_ghosts):
                ghost_Y[j] = 2000
            game_over_text()
            break


    # motion of missile
    if missile_state == 'launch':
        launch_missile(missile_X, missile_Y)
        missile_Y -= missile_Y_change

    if missile_Y < 0:
        missile_Y = 520
        missile_state = 'load'



    # Level 1 completes if score reaches 1000
    if score_value >= 1000:
        level_complete()
        carry_on = False