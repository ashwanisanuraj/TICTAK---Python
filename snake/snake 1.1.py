# to give graphics to the snake
# we need to cycle through every block in snake.body, and relate how the block reacts with previous block there

import pygame, sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        # to get graphical image of snake wee need to get it for up,down,left,rigth for head, body and tail
        self.head_up = pygame.image.load('Python\snake\Graphics\head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Python\snake\Graphics\head_down.png').convert_alpha()
        self.head_left = pygame.image.load('Python\snake\Graphics\head_left.png').convert_alpha()
        self.head_right = pygame.image.load('Python\snake\Graphics\head_right.png').convert_alpha()

        self.tail_up = pygame.image.load('Python\snake\Graphics\Tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Python\snake\Graphics\Tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('Python\snake\Graphics\Tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('Python\snake\Graphics\Tail_right.png').convert_alpha()

        self.body_vertical = pygame.image.load('Python\snake\Graphics\Body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Python\snake\Graphics\Body_horizontal.png').convert_alpha()

        # curve body part
        self.body_tr = pygame.image.load('Python\snake\Graphics\Body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Python\snake\Graphics\Body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Python\snake\Graphics\Body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Python\snake\Graphics\Body_bl.png').convert_alpha()

    def draw_snake(self):
        # 3. 
        self.update_head_graphics()
        self.update_tail_graphics()

        # for block in self.body:
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)
        #     block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        #     pygame.draw.rect(screen,(183,111,122),block_rect)

        # first we want to look for every block in snake body
        for index,block in enumerate(self.body):  # we want to look at more thing then just the block, we need to look at the block before and after, so we use enumarate. enumarate gives us an index on which object we r in inside the block
            # 1. we need a rect for the positioning
            # 2. what direction is theface headiing
            # 1. 
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            # 2. 
            if index == 0:
                # screen.blit(self.head_right,block_rect) # after step 3. 
                screen.blit(self.head,block_rect)

                # 3. snake head direction not updating
            elif index == len(self.body) - 1:  # elif index = last item in self.body
                screen.blit(self.tail,block_rect)

            else: #for middle body
                previous_block = self.body[index + 1] - block # we r indexing from self (index is going to be our current element).body and then add one or sub to get to next or previous block
                next_block = self.body[index - 1] - block
                # we have to check previos block and next block r at the same x and y coordinate. the block between them will be verticle or horizontal
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)

                # for turning, 
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)


            # else:
            #     pygame.draw.rect(screen,(150,100,100),block_rect)

    def update_head_graphics(self): # we will subtract the head to the item that comes just next to it. 
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down


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
        screen.blit(apple,fruit_rect)         

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

    def draw_score(self): 
        score_text = str(len(self.snake.body) - 3) 
        score_surface = game_font.render(score_text,True,(56,74,12)) 
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40) 
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)

        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)



pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Python\snake\Graphics\Apple.png').convert_alpha()
game_font = pygame.font.Font('Python\snake\Font\hp.ttf', 25) 


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

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