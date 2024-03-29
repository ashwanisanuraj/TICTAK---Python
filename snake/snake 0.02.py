#creating a rectangle(fruit)
import pygame, sys,random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        # self.x = 5
        # self.y = 4
        self.x = random.randint(0,cell_number - 1)  
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)
        #create an x and y poition
        #draw a square

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size) #drawing the rectangle fruit, pygameRect(x cordinate,y cordinate,width,height)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)            #we r drawing a fruit rectangle. pygame.draw.rect(surface to draw,color of rect,name of rect(fruit_rect here))


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT() #to call the FRUIT; to draw on screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill((175,215,70))
    fruit.draw_fruit() # to actually see it on our screen
    pygame.display.update()
    clock.tick(60)