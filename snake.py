import pygame
import random

class Snake():
    def __init__(self,screen,swidth,sheight) -> None:
        self.x = swidth // 2
        self.y = sheight // 2
        self.body = [[self.x,self.y]]
        self.size = 1
        self.direction = -1
        self.score = 0
        self.snakesize = 10
        self.step = 10
        pygame.draw.rect(screen,"black",pygame.Rect(self.x,self.y,self.snakesize,self.snakesize))


    def draw(self) -> None:
        for i in self.body:
            pygame.draw.rect(screen,"white",pygame.Rect(i[0],i[1],self.snakesize,self.snakesize))    

    def control(self) -> None:
        if key[pygame.K_UP]:
            self.direction = self.direction if self.direction == -90 else 90
        elif key[pygame.K_DOWN]:
            self.direction = self.direction if self.direction == 90 else -90
        elif key[pygame.K_LEFT]:
            self.direction = self.direction if self.direction == 0 else 180
        elif key[pygame.K_RIGHT]:
            self.direction = self.direction if self.direction == 180 else 0
    
    def play(self,dt) -> None:
        match self.direction:
            case 0 :
                self.x += self.step
            case -90:
                self.y += self.step
            case 180:
                self.x -= self.step 
            case 90:
                self.y -= self.step

        self.draw()
        self.control()
        self.body.insert(0,[self.x,self.y])
        
    def collision(self,swidth,sheight,mekla):
        if self.y < 0:
            self.y = sheight
            self.direction = 90
        elif self.y > sheight:
            self.y = 0
            self.direction = -90
        elif self.x < 0:
            self.x = swidth
            self.direction = 180
        elif self.x > swidth:
            self.x = 0
            self.direction = 0

        if mekla.x == self.x and mekla.y == self.y:    
            mekla.reset(screen.get_width(),screen.get_height())
            self.score += 10
        else:
            self.body.pop()

        for b in self.body[1:]:
            if b[0] == self.x and b[1] == self.y:
                pygame.quit()        

class Mekla():
    def __init__(self,screen,swidth,sheight) -> None:
        self.x = random.randrange(1, (swidth//10)) * 10
        self.y = random.randrange(1, (sheight//10)) * 10
        self.meklasize = 10


    def draw(self,screen):
        pygame.draw.rect(screen,"green",pygame.Rect(self.x,self.y, self.meklasize, self.meklasize))

    def reset(self,swidth,sheight):
        self.x = random.randrange(1, (swidth//10)) * 10
        self.y = random.randrange(1, (sheight//10)) * 10
        


pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
run = True
dt = 0
snake = Snake(screen,screen.get_width(),screen.get_height())
mekla = Mekla(screen,screen.get_width(),screen.get_height())

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("black")
    
    score  = "Score : {}".format(snake.score)
    font = pygame.font.SysFont('Comic Sans MS', 30)
    textscore = font.render(score,False,"white")
    screen.blit(textscore,(0,0))

    key = pygame.key.get_pressed()

    snake.play(dt)
    snake.collision(screen.get_width(),screen.get_height(),mekla)
    mekla.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 100
    pygame.time.Clock().tick(15)

pygame.quit()