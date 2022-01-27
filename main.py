from ast import Pass
import pygame
from pygame.locals import *

#Função que desenha um bloco:
def draw_block():
    surface.fill((110,110,5))
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()



if __name__ == "__main__":
    pygame.init()

    # Abre a janela do jogo, coloca cor e manda para a tela
    surface = pygame.display.set_mode((500,500))
    surface.fill((92,50,84))

    block = pygame.image.load("resources/block.jpg").convert()
    block_x, block_y = 100, 100
    surface.blit(block, (block_x,block_y))

    pygame.display.flip()

    #Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
