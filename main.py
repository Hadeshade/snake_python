from ast import For, Pass
from ctypes.wintypes import SIZE
import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,24)*SIZE
        self.y = random.randint(0,19)*SIZE

class Snake:
    #Definições inicias da classe o self é o this, parent_screen é herença de outra classe e lenght parametro;
    def __init__(self, parent_screen, lenght):
        self.lenght = lenght
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*lenght
        self.y = [SIZE]*lenght
        self.direction = 'down'

    def increase_length(self):
        self.lenght+=1
        self.x.append(-1)
        self.y.append(-1)

    # Desenha todo o tamanho da cobra
    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.lenght):
            self.parent_screen.blit(self.block, (self.x[i],self.y[i]))
        pygame.display.flip()

    #Apenas define a direção que deve se movimentar
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_down(self):
        self.direction = 'down'
    def move_up(self):
        self.direction = 'up'

    def walk(self):

        #Coloca a posição do último quadrado no proximo (faz a movimentação)
        for i in range(self.lenght-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        #Lógica para movimentar os quadrados (a cobra)
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE

        self.draw()
    
    
class Game:
    def __init__(self):
        pygame.init()   

        # Abre a janela do jogo, coloca cor e manda para a tela
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((92,50,84))
        #Cria objeto Snake e desenha ela:
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        #Cria objeto maça:
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1,y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        return False



    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.lenght}", True, (200,200,200))
        self.surface.blit(score, (800,10))

    def run(self):
        #Loop principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()

    
