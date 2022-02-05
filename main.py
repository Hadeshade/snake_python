from ast import For, Pass
from ctypes.wintypes import SIZE
import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110,110,5)

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
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

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
        #self.parent_screen.fill(BACKGROUND_COLOR)
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


        pygame.mixer.init()
        #Inicializa musica do jogo:
        self.play_background_music()
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

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def play_sound(self, music):
        sound =pygame.mixer.Sound(f"resources/{music}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):

        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Colisão com maça
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        #Colisão com a própria cobra
        for i in range(3,self.snake.lenght):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.play_sound("crash")
                raise "Game over"

        #Colisão com paredes (futuro):
        

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.lenght}", True, (200,200,200))
        self.surface.blit(score, (800,10))

    #Mensagem de Game Over:
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        linel = font.render(f"Score: {self.snake.lenght}", True, (255,255,255))
        self.surface.blit(linel, (200,300))
        line2 = font.render("Para jogar novamente aperte Enter, para sair aperte Esc!", True, (255,255,255))
        self.surface.blit(line2, (200,200))
        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface,2)
        self.apple = Apple(self.surface)

    def run(self):
        #Loop principal
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    
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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()

    
