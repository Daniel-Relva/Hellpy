import pygame
from pygame.locals import *
import os
import random
import math
from Imagens import *


class Heroi:
  IMGS = IMAGENS_HEROI
  VIDA_MAX = 3
  TEMPO_ANIMACAO = 5 #frames para mudar a imagem e criar uma animação

  def __init__(self, x, y, vida, angulo):
    self.x = x
    self.y = y
    self.vida = vida
    self.angulo = angulo
    self.velocidade = 1
    self.cont_imagem = 0
    self.cont = 0
    self.tempo = 0
    self.imagem = self.IMGS[0]
    self.imagem_rot = pygame.transform.rotate(self.imagem, self.angulo)

  def mover(self,move, contorno, objetos, heroi):

    move_right,move_left,move_up,move_down = move

    if(move_right) and self.x < (TELA_LARGURA-contorno.right.get_width()-self.imagem.get_width()):
      self.x += 10
      self.tempo += 1
    if(move_left) and self.x > contorno.left.get_width():
      self.x -= 10
      self.tempo += 1
    if(move_down) and self.y < (TELA_ALTURA-contorno.base.get_height()-self.imagem.get_height()):
      self.y += 10
      self.tempo += 1
    if(move_up) and self.y > contorno.left.get_width():
      self.y -= 10
      self.tempo += 1
    if not move_left and not move_right and not move_down and not move_up:
      self.tempo=0
    
  
  def rotacionar(self, spin):
    
    move_clockwise, move_counterclock = spin

    if move_clockwise and self.angulo <= 360:
      self.angulo += 2
    if move_counterclock:
      self.angulo -=2
    if self.angulo > 360:
      self.angulo = 0

    self.imagem_rot = pygame.transform.rotate(self.imagem, self.angulo)

  def desenhar (self, tela):
    #definir qual imagem do heroi
    self.cont_imagem += 1

    # dar o efeito de mover as pernas enquanto anda
    if self.cont_imagem < self.TEMPO_ANIMACAO:
      self.imagem = self.IMGS[0]
    elif self.cont_imagem < self.TEMPO_ANIMACAO*2:
      self.imagem = self.IMGS[1]
    elif self.cont_imagem < self.TEMPO_ANIMACAO*3:
      self.imagem = self.IMGS[0]
    elif self.cont_imagem < self.TEMPO_ANIMACAO*4:
      self.imagem = self.IMGS[2]
    elif self.cont_imagem >= self.TEMPO_ANIMACAO*4 + 1:
      self.imagem = self.IMGS[0]
      self.cont_imagem = 0

    #se tiver parado as pernas n trocam de posicao
    if self.tempo == 0:
      self.imagem = self.IMGS[0]

    #desenhar a imagem na tela
    pos_centro_imagem = self.imagem_rot.get_rect(topleft=(self.x, self.y)).center
    retangulo = self.imagem_rot.get_rect(center=pos_centro_imagem)
    tela.blit(self.imagem_rot, retangulo.topleft)

  def get_mask(self):
    return pygame.mask.from_surface(self.imagem_rot)

  def colidir_h_v(self,vilao):

    vilao3_mask = vilao.get_maskv()
    heroi_mask = pygame.mask.from_surface(self.imagem_rot)

    bateu_v3 = vilao3_mask.overlap(heroi_mask,(round(self.x) - round(vilao.xv),round(self.y) - round(vilao.yv)))

    if bateu_v3:
      return True
    else:
      return False

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

class Vilao:
  IMGSv = IMAGENS_VILAO
  TEMPO_ANIMACAOv = 5

  def __init__ (self, xv, yv, forca,number, angulo):
    self.number = number
    self.xv = xv
    self.yv = yv
    self.forca = forca
    self.cont_imagemv = 0
    self.tempo = 0
    self.angulov = angulo
    self.img_listav = self.IMGSv[self.number]
    self.imagemv = self.img_listav[0]


  def moverv(self,contorno,muda_dir, muda_dir2):# muda_dir3):
    self.velocidade = 3
    aux_lista = []
    
    self.tempo += 1

    if self.cont_imagemv == self.TEMPO_ANIMACAOv:

      if self.yv <= contorno.topo.get_height() or muda_dir or muda_dir2:# or muda_dir3:
        self.angulov = random.randrange(180,360)

      if self.yv >= TELA_ALTURA - contorno.base.get_height() - self.imagemv.get_height() or muda_dir or muda_dir2:# or muda_dir3:
        self.angulov = random.randrange(0,180)

      if self.xv <= contorno.left.get_width() or muda_dir or muda_dir2:# or muda_dir3:
        aux_lista = [random.randrange(0,90), random.randrange(270,360)]
        self.angulov = aux_lista[random.randrange(0,1)]

      if self.xv >= TELA_LARGURA - contorno.right.get_width() - self.imagemv.get_width() or muda_dir or muda_dir2:# or muda_dir3:
        self.angulov = random.randrange(90,270)

    self.m = math.tan(math.radians(self.angulov)) #coeft. angular da reta

    if self.angulov > 0 and self.angulov <= 67.5:
      self.xv += self.velocidade
      self.yv -= (self.velocidade * self.m) #equaç. da reta

    if self.angulov > 67.5 and self.angulov <= 112.5:
      self.xv += 0
      self.yv -= self.velocidade

    if self.angulov > 112.5 and self.angulov <= 247.5:
      self.xv -= self.velocidade
      self.yv += (self.velocidade * self.m)

    if self.angulov > 247.5 and self.angulov <= 292.5:
      self.xv -= 0
      self.yv += (self.velocidade)

    if self.angulov > 292.5 and self.angulov <= 360:
      self.xv += self.velocidade
      self.yv += (self.velocidade * (self.m)*(-1))


  def desenharv(self, tela):
    self.cont_imagemv +=1

    if self.cont_imagemv < self.TEMPO_ANIMACAOv:
      self.imagemv = self.img_listav[0]
    elif self.cont_imagemv < self.TEMPO_ANIMACAOv*2:
      self.imagemv = self.img_listav[1]
    elif self.cont_imagemv >= self.TEMPO_ANIMACAOv*2 + 1:
      self.imagemv = self.img_listav[0]
      self.cont_imagemv = 0

    imagem_rotv = pygame.transform.rotate(self.imagemv, self.angulov)
    pos_centro_imagemv = self.imagemv.get_rect(topleft=(self.xv,self.yv)).center
    retv = imagem_rotv.get_rect(center=pos_centro_imagemv)
    tela.blit(imagem_rotv, retv.topleft)

  def get_maskv(self):
    return pygame.mask.from_surface(self.imagemv)
  
#---------------------------------------------------------
#-----------------------------------------------------
class Poder:
  IMGp = IMAGEM_PODER

  def __init__(self, heroi):
    angulop = heroi.angulo
    self.angulop = angulop
    self.xp = heroi.x
    self.yp = heroi.y
    self.tempo = 0
    self.imagemp = self.IMGp
    self.velocidadep = 4

  def moverp(self):
    if self.angulop < 0:
      self.angulop = 360 + self.angulop

    self.tempo += 1

    self.mp = math.tan(math.radians(self.angulop)) #coeft. angular da reta

    if self.angulop >= 0 and self.angulop <= 67.5:
      self.xp += self.velocidadep
      self.yp -= (self.velocidadep * self.mp) #equaç. da reta

    if self.angulop > 67.5 and self.angulop <= 112.5:
      self.xp += 0
      self.yp -= self.velocidadep

    if self.angulop > 112.5 and self.angulop <= 247.5:
      self.xp -= self.velocidadep
      self.yp += (self.velocidadep * self.mp)

    if self.angulop > 247.5 and self.angulop <= 292.5:
      self.xp -= 0
      self.yp += (self.velocidadep)

    if self.angulop > 292.5 and self.angulop <= 360:
      self.xp += self.velocidadep
      self.yp += (self.velocidadep * (self.mp)*(-1))

  def desenharp(self,tela):
    imagem_rotp = pygame.transform.rotate(self.imagemp,self.angulop)
    pos_centro_imagemp = self.imagemp.get_rect(topleft = (self.xp,self.yp)).center
    retp = imagem_rotp.get_rect(center=pos_centro_imagemp)
    tela.blit(imagem_rotp, retp.topleft)

  def colidir_v(self,vilao):
    vilao2_mask = vilao.get_maskv()
    poder_mask = pygame.mask.from_surface(self.imagemp)

    bateu_v2 = vilao2_mask.overlap(poder_mask,(round(self.xp) - round(vilao.xv),round(self.yp) - round(vilao.yv)))

    if bateu_v2:
      return True
    else:
      return False