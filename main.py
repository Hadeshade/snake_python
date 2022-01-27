from ast import For, Pass
from ctypes.wintypes import SIZE
import pygame
from pygame.locals import *
import time

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x,self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, lenght):
        self.lenght = lenght
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*lenght
        self.y = [SIZE]*lenght
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.lenght):
            self.parent_screen.blit(self.block, (self.x[i],self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_down(self):
        self.direction = 'down'
    def move_up(self):
        self.direction = 'up'

    def walk(self):

        for i in range(self.lenght-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

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
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        #Cria objeto maça:
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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

            time.sleep(0.3)

if __name__ == "__main__":
    game = Game()
    game.run()

    
