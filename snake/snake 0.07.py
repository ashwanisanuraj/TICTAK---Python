# adding score
# create a font object, create text with the font object, blit the text on the display surface

import pygame, sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
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
            self.new_block = False
        else:
            body_copy = self.body[:-1] 
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
       self.randomize()


    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size) 
        pygame.draw.rect(screen,(126,166,114),fruit_rect)           

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)  
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN: 
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self): 
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self): 
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: 
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        # 2 ways. 1.snake is outside the screen, 2.snake hits itself
        #1.
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        #2.
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self): # for score we will check teh length of the snake
        score_text = str(len(self.snake.body) - 3) # initial size of snake is 3 so - 3
        score_surface = game_font.render(score_text,True,(56,74,12)) # score_surface = game_font.render(text(score text),aa(anti alias text)-it is used to make the text little smoother[true or false],color(for right now we will use RGB(56,74,12)))
        score_x = int(cell_size * cell_number - 60) # we r positioning the score board. cell_size*xell_number will give us right end of the screen, and from that we will remove couple of pixels(60), that means we r going to the right end of the screen and a bit left
        score_y = int(cell_size * cell_number - 40) # all the way down but little up
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        #to put on screen
        # screen.blit(score_surface,position)
        screen.blit(score_surface,score_rect)



pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font('Python\snake\Font\hp.ttf', 25) # this will initiate the font, syntax: game_font = pygame.font.Font(font name,font size)

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
                if main_game.snake.direction.y != 1: 
                    main_game.snake.direction = Vector2(0,-1) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
        
        



    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)