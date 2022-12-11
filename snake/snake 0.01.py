#intall pygame; pip intall pygame

import pygame        # to import pygame
import sys           # for system functions(sys.exit)
pygame.init()        # it starts the pygame; pygame contains different types of modules for graphics, sounds, excetra

screen = pygame.display.set_mode((400,500))  # dispaly is the main screen of the game, it needs to be stored in a variable(screen) 

clock = pygame.time.Clock()       # this will create clock object, this object will help us manipulate time in pygame

# pygame.Surface((100,200))    # we are creating a test screen with width and height (100,200)
test_surface = pygame.Surface((100,200))
test_surface.fill(pygame.Color('blue'))
# test_rect = pygame.Rect(100,200,100,100)    # pygame.Rect(x,y,width,height)
test_rect = test_surface.get_rect(center = (200,250))    # this will get the surface and put a rectangle around it, it also gives option where to draw the rectangle(center)
while True:    # the 'screen' opened for slight seconds, now we create while loop to keep it open
     # we r going to draw all elements(snack, bg, excetra)
    pygame.display.update() # will make the bg screen stay open

    clock.tick(60)   #this will run our game at 60, and never cross it; clock.tick(FrameRate)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # these code will help us quit the bg screen(else the bg screen will be running infinately)

            # right now our game is running at max(as much as our cpu can provide)

    # in pygame there r two display, 1. surfaces(a layer that can display graphics, there is only multiple, it is not displayed by default)
    # 2. display surface(the canvas the entire game is drawn on, there is only one, it is displayed by default)
    # if we want to use surfaces for different elements; 1. create a surface(import an image, write text, or create an empty space)
    # 2. display the surface(this could be the disaplay surface or the regular surfaces)

    screen.fill((175,215,70))

    # pygame.draw.rect(screen, pygame.Color('gold'), test_rect)  # draw.rect(a surface to draw(screen),color, a rectangle(test_rect))
    # screen.blit(test_surface,(200,250))      # pygame.blit(surface,(weidth,height))-tuple(x,y); blit = block image transfer; to put the test_surface on screen
    screen.blit(test_surface,test_rect) # we r placing the rectangle on the surface(screen)



    # still we cant see the screen because both bg and screen are black colored
    # to change it we use the fill function
    # screen.fill(pygame.Color('green')), we had to place screen.fill above sceen.blit
    # color is based on RGB(RED, GREEN, BLUE)->max_value(255); we can make a new color by given values to rgb as (175,215,70)-> 175,red 215,green 70,blue
    # creating a rect; pygame.Rect(x,y,w,h) -> new rect
    # surface.get_rect(position)
    #-> rect around surface
       