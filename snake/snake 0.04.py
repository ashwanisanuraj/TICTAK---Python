# movement of snake
# the head moves to a new block, each block moves to the position of block that used to be before it(this deletese the last block)


import pygame, sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        body_copy = self.body[:-1] # this copies the self.body vector2 excluding the last vector
        body_copy.insert(0,body_copy[0] + self.direction) # for head, we r inserting a new direction for the head to move in
        self.body = body_copy[:] # to copy the new body to the old(to display on screen)


class FRUIT:
    def __init__(self):
        # self.x = 5
        # self.y = 4
        self.x = random.randint(0,cell_number - 1)  
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)
       
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size) 
        pygame.draw.rect(screen,(126,166,114),fruit_rect)           


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT() 
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
# this is a custom event triggered by timer(in millisecs), and in events we can capture it.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if  event.type == SCREEN_UPDATE:
            snake.move_snake()
            # after catching the custom event we call the snake movement
        if event.type == pygame.KEYDOWN: # this is going to be trigered whenever we press any button on the keyboard
            if event.key == pygame.K_UP: # k_UP is the up key in our keyboard
                snake.direction = Vector2(0,-1) # after pressing K_UP we want to do smtg(call direction)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
        
        



    screen.fill((175,215,70))
    fruit.draw_fruit() 
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)