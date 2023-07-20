import pygame
from pygame.locals import *
import os
import random
import math

TELA_LARGURA = 1000
TELA_ALTURA = 600
CONT = 0

pygame.font.init() #Iniciei a fonte
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
FONTE_TIME = pygame.font.SysFont('arial', 50)
FONTE_VIDA = pygame.font.SysFont('arial',50)
FONTE_BG = pygame.font.SysFont('arial', 50)

#----------------------------------------
#-------------------------------------------


IMAGENS_HEROI = [pygame.image.load(os.path.join('imagem', 'heroi1.png')),#Caso seja necessário mudar o tamanho da imagem pode-se utilizar pygame.transform.scale2x(...)
                 pygame.image.load(os.path.join('imagem', 'heroi2.png')),
                 pygame.image.load(os.path.join('imagem', 'heroi3.png'))] #São 3 pois é para dar a ideia de movimento, podemos tirar isso dps e deixar só um
                                   
IMAGENS_VILAO = [[pygame.image.load(os.path.join('imagem', 'vilao1.png')),
                 pygame.image.load(os.path.join('imagem', 'vilao2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'vilao3.png')),
                  pygame.image.load(os.path.join('imagem', 'vilao4.png'))],
                 [pygame.image.load(os.path.join('imagem', 'vilao5.png')),
                  pygame.image.load(os.path.join('imagem', 'vilao6.png'))],
                 [pygame.image.load(os.path.join('imagem', 'vilao7.png')),
                  pygame.image.load(os.path.join('imagem', 'vilao8.png'))],
                 [pygame.image.load(os.path.join('imagem', 'vilao9.png')),
                  pygame.image.load(os.path.join('imagem', 'vilao10.png'))],
                 [pygame.image.load(os.path.join('imagem', 'vilao11.png')),
                  pygame.image.load(os.path.join('imagem', 'vilao12.png'))]]#Vilão pensei em fazer flutando msm pra ficar mais facil, mas coloquei 3 para ter variedade

IMAGEM_PODER = pygame.image.load(os.path.join('imagem', 'poder.png')) #deixei com um poder só, mas podemos adicionar mais
                                   
IMAGENS_CENARIO = [pygame.image.load(os.path.join('imagem', 'objeto1.png')),
                   pygame.image.load(os.path.join('imagem', 'objeto2.png')),
                   pygame.image.load(os.path.join('imagem', 'objeto3.png'))]#Variedade de objetos que irão compor o cenario

IMAGENS_BORDA = [[pygame.image.load(os.path.join('imagem', 'parede1_1.png')),
                 pygame.image.load(os.path.join('imagem', 'parede1_2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'parede2_1.png')),
                 pygame.image.load(os.path.join('imagem', 'parede2_2.png'))]]#2 tipos de paredes diferentes para as bordas em fazer flutando msm pra ficar mais facil, mas coloquei 3 para ter variedade

IMAGENS_PORTA = [[pygame.image.load(os.path.join('imagem', 'p1.png')),
                 pygame.image.load(os.path.join('imagem', 'p2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'p3.png')),#O que dará acesso a próxima sala
                  pygame.image.load(os.path.join('imagem', 'p4.png'))]]

IMAGENS_VIDA = [pygame.image.load(os.path.join('imagem','vida1.png')),
                pygame.image.load(os.path.join('imagem','vida2.png'))]

IMAGENS_BACKGROUND = pygame.image.load(os.path.join('imagem', 'bg.png'))

IMAGENS_SANGUE = [[pygame.image.load(os.path.join('imagem', 'S1.png'))],#Caso seja necessário mudar o tamanho da imagem pode-se utilizar pygame.transform.scale2x(...)
                 [pygame.image.load(os.path.join('imagem', 'S2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'S3.png'))]]

