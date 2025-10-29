import pygame
from pygame.locals import *
from sys import exit
from os.path import join
import random

#Setup geral
pygame.init()
LARGURA_TELA, ALTURA_TELA = 920, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
#renomeia o que aparece como nome da janela do jogo
pygame.display.set_caption('Sr Bracat & o Pósitron')
running = True
clock = pygame.time.Clock()

#imports/personagens/itens gráficos
sr_Bracat_surf = pygame.image.load(join('images', 'SrBracat.png')).convert_alpha()
sr_Bracat_rect = sr_Bracat_surf.get_rect(center=(LARGURA_TELA/2, ALTURA_TELA/2))
positron_surf = pygame.image.load(join('images', 'positron.png')).convert_alpha()
positron_rect = positron_surf.get_rect(bottomleft=(LARGURA_TELA/2, ALTURA_TELA/2))

#o jogo sempre fica dentro de um loop (acho que da mesma forma que o arduino). O jogo inteiro fica dentro do loop
while running:
    clock.tick(12)
    for event in pygame.event.get():
        #condição que para o programa caso a janela seja fechada
        if event.type == QUIT:
            running = False
    #a cada iteração do loop, a tela é atualizada
    tela.fill('darkslategray3')
    tela.blit(positron_surf, positron_rect)
    positron_rect.left += 15
    positron_rect.top += 15
    tela.blit(sr_Bracat_surf, sr_Bracat_rect)
    sr_Bracat_rect.left -= 15
    sr_Bracat_rect.top -= 15
    pygame.display.update()
pygame.quit()