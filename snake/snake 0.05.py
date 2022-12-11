# connect the snake and the fruit
# for this we need a logic, we will create a main class which will contain the entire logic of our game and also contain the snake and fruit objects


import pygame, sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] 
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body = body_copy[:] 
            # this will keep incresing the snake infinitly so we need to make this false
            self.new_block = False
        else:
            body_copy = self.body[:-1] 
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True




class FRUIT:
    def __init__(self):
        # self.x = 5
        # self.y = 4
        # self.x = random.randint(0,cell_number - 1)  
        # self.y = random.randint(0,cell_number - 1)
        # self.pos = Vector2(self.x,self.y)
       self.randomize()


    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size) 
        pygame.draw.rect(screen,(126,166,114),fruit_rect)           

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)  
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)


class MAIN: # all the important functions will be coded here
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self): # to move the snake
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self): # here we will code all the elements which we need to draw on the screen
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: # snake.body[0] is the head of the snake, if the head gets in same locaton as the fruit rectangle
            # print('snack') # if we get a collision a print will come; before running we need to call this collision fn in the main->update(self)
            # no of things we wanna do then snack collids with fruit; 1. reposition the fruit, 2.add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if  event.type == SCREEN_UPDATE:
            main_game.update()
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: 
                main_game.snake.direction = Vector2(0,-1) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
        
        



    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)