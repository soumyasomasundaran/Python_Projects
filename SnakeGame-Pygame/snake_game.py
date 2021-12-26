import pygame,sys
import random,time

pygame.init()


WIDTH = 900
HEIGHT = 600
dis = pygame.display.set_mode((WIDTH, HEIGHT))
game_close = False
snake_block = 30
clock = pygame.time.Clock()

is_eaten = False
score = 0
gameover = False
hasPlayedGameOverSound =  False
pygame.mixer.music.load('music/monkey.mp3')
pygame.mixer.music.play(-1)


def display_score():
    font  = pygame.font.SysFont('Tlwg Typist',30)
    score_font = font.render(f'score: {score}',True, (255,255,255))
    font_pos = score_font.get_rect(center=(WIDTH //2-40 , 30))
    dis.blit(score_font,font_pos)

def end_screen(): 
    font  = pygame.font.SysFont('Tlwg Typist',80)
    score_font = font.render(f'GAME OVER !!', True, 'blue')
    font_pos = score_font.get_rect(center=(WIDTH //2-40 , HEIGHT//2))
    dis.blit(score_font,font_pos)
    bg = pygame.image.load("images/bg.png")
    dis.blit(bg, (0, 0))
    display_score() 
    


    

def draw_grid():
    for x in range(0,WIDTH,snake_block):
        for y in range(0,HEIGHT,snake_block):
            rect = pygame.Rect(x, y, snake_block, snake_block) # creating a rectangle object
            pygame.draw.rect(dis,'#404040',rect,1)


class Snake:
    def __init__(self):
        self.x  = 300
        self.y = 300 # make sure this is a multiple of 30
        self.body = [pygame.Rect(self.x, self.y,snake_block,snake_block)]
        self.direction = 'none'
        self.head = self.body
        

    def draw_snake(self):    
        for block in self.body:
            pygame.draw.rect(dis,'green',block)


    def move_left(self):
        self.direction = 'left'    
    def move_right(self):
        self.direction = 'right'
    def move_down(self):
        self.direction = 'down'    
    def move_up(self):
        self.direction = 'up'
    
    def update_snake(self):
        self.body.append(pygame.Rect(self.x, self.y, snake_block,snake_block))     
        self.head = self.body[-1]

    def move(self):    
        if self.direction =='right':
            self.x += snake_block
        if self.direction =='left':
            self.x -= snake_block
        if self.direction =='down':
            self.y += snake_block
        if self.direction =='up':
            self.y -= snake_block
        self.update_snake()
        
              
    def is_gameover(self):
        global gameover
        for block in self.body[1:]:
            if block.colliderect(snake.body[0]):
                    gameover = True
        if self.head.x <=0 or self.head.x >= WIDTH:
            gameover = True
        if self.head.y+10 <=0 or self.head.y >= HEIGHT:
            gameover = True
          
class Fruit:
    def __init__(self):
        self.x = int(random.randint(0,WIDTH)//snake_block) * snake_block
        self.y =  int(random.randint(0,HEIGHT)//snake_block) *snake_block
        
    
    def draw_fruit(self):
        self.body = pygame.Rect(self.x, self.y,snake_block,snake_block) 
        pygame.draw.rect(dis,'red',self.body)
    
    def get_random_pos(self):
        self.x = int(random.randint(0,WIDTH)//snake_block) *snake_block
        self.y =  int(random.randint(0,HEIGHT)//snake_block) *snake_block

    
        
       


snake = Snake()
fruit = Fruit()


while not game_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.move_left()
            if event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.move_right()
            if event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.move_down()
            if event.key == pygame.K_UP and snake.direction!='down':
                snake.move_up()
    dis.fill((0,0,0))
    draw_grid()
    snake.draw_snake()
    snake.move()  
    fruit.draw_fruit()


    if (snake.head).colliderect(fruit.body):
        is_eaten = True
        score +=10
    else:
        snake.body.pop(0)

    if is_eaten:
        fruit.get_random_pos()
        is_eaten = False

    fruit.draw_fruit()
    snake.is_gameover()
    if gameover:
        pygame.mixer.music.stop()
        dis.fill('black')
        end_screen()  

    display_score()
    pygame.display.update()
    clock.tick(5)
