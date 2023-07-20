import pygame
from pygame.locals import *
import os
import random
import math
from Imagens import *

class Contorno:
  IMGc = IMAGENS_BORDA

  def __init__ (self):
    self.grupo = random.randrange(0,len(self.IMGc))
    self.imagemc = self.IMGc[self.grupo]
    self.topo = self.imagemc[0]
    self.base = self.imagemc[0]
    self.left = self.imagemc[1]
    self.right = self.imagemc[1]

  def desenharc(self, tela):
    tela.blit(self.topo,(0,0))#topo
    tela.blit(self.base, (0,TELA_ALTURA-50))#Base
    tela.blit(self.left, (0,0))#esquerda
    tela.blit(self.right, (TELA_LARGURA-50,0))#Direita
##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

class Portal:
  IMGport = IMAGENS_PORTA
  TEMPO_ANIMACAOport = 5

  def __init__(self,xport,yport):
    self.lista_imagemport = self.IMGport[random.randrange(0,len(self.IMGport))]
    self.imagemport = self.lista_imagemport[0]
    self.xport = xport
    self.yport = yport
    self.cont_imagem_port = 0

  def desenharport(self,tela):
    self.cont_imagem_port +=1

    if self.cont_imagem_port < self.TEMPO_ANIMACAOport:
      self.imagemport = self.lista_imagemport[0]
    elif self.cont_imagem_port < self.TEMPO_ANIMACAOport*2:
      self.imagemport = self.lista_imagemport[1]
    elif self.cont_imagem_port >= self.TEMPO_ANIMACAOport*2 + 1:
      self.imagemport = self.lista_imagemport[0]
      self.cont_imagem_port = 0

    pos_centro_imagemport = self.imagemport.get_rect(topleft=(self.xport,self.yport)).center
    retport = self.imagemport.get_rect(center=pos_centro_imagemport)
    tela.blit(self.imagemport, retport.topleft)

  def colidir_portal_h(self, heroi):
    heroi_mask4 = heroi.get_mask()
    portal_mask = pygame.mask.from_surface(self.imagemport)

    entrou_h = heroi_mask4.overlap(portal_mask,(round(self.xport) - round(heroi.x),round(self.yport)-round(heroi.y)))

    if entrou_h:
      return True
    else:
      return False

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

class Objetos:
  IMGo = IMAGENS_CENARIO

  def __init__ (self, xo, yo, anguloo):
    self.imagemo = self.IMGo[random.randrange(0,len(self.IMGo))]
    self.xo = xo
    self.yo = yo
    self.anguloo = anguloo
    self.imagem_roto = pygame.transform.rotate(self.imagemo, self.anguloo)


  def desenharo(self,tela):
    pos_centro_imagem_o = self.imagem_roto.get_rect(topleft=(self.xo,self.yo)).center
    retangulo_o = self.imagem_roto.get_rect(center=pos_centro_imagem_o)
    tela.blit(self.imagem_roto, retangulo_o)

    

  def colidir_o_H(self,heroi):
    heroi_mask2 = heroi.get_mask()
    obj_mask2 = pygame.mask.from_surface(self.imagem_roto)

    bateu_h = heroi_mask2.overlap(obj_mask2, ((round(self.xo) - round(heroi.x)-10,round(self.yo) - round(heroi.y)-10)))

    if bateu_h:
      return True
    else:
      return False

  def colidir_o_v(self,vilao):
    vilao_mask = vilao.get_maskv()
    obj_mask = pygame.mask.from_surface(self.imagem_roto)


    bateu_v = vilao_mask.overlap(obj_mask, (round(self.xo) - round(vilao.xv)-10,round(self.yo) - round(vilao.yv)-10))#distancia)

    if bateu_v:
      return True
    else:
      return False
##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

class Placar:

  IMGvi = IMAGENS_VIDA
  PONTOS = FONTE_PONTOS

  def __init__(self,vida,pontos):
    self.imagemvida = self.IMGvi
    self.texto = self.PONTOS
    self.pontos = pontos
    self.vida = vida

  def desenharplacar(self,tela):
    text = self.texto.render(f"Score:{self.pontos}",1,(255,255,255))#esse 255 é a cor rgb

    if self.vida == 3:
      imagem1 = self.imagemvida[0]
      imagem2 = self.imagemvida[0]
      imagem3 = self.imagemvida[0]
    elif self.vida == 2:
      imagem1 = self.imagemvida[1]
      imagem2 = self.imagemvida[0]
      imagem3 = self.imagemvida[0]
    elif self.vida == 1:
      imagem1 = self.imagemvida[1]
      imagem2 = self.imagemvida[1]
      imagem3 = self.imagemvida[0]
    else:
      imagem1 = self.imagemvida[1]
      imagem2 = self.imagemvida[1]
      imagem3 = self.imagemvida[1]
      
    tela.blit(text, (TELA_LARGURA - 10 - text.get_width(),10))
    tela.blit(imagem1, (TELA_LARGURA - text.get_width() - imagem1.get_width() - 20,10))
    tela.blit(imagem2, (TELA_LARGURA - text.get_width() - imagem1.get_width() - imagem2.get_width() - 30,10))
    tela.blit(imagem3, (TELA_LARGURA - text.get_width() - imagem1.get_width() - imagem2.get_width() - imagem3.get_width() - 40,10))
##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------




