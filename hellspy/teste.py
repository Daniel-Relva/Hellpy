import pygame
from pygame.locals import *
import os
import random
import math
## Bibliotecas necessárias para rodar o jogo.


TELA_LARGURA = 1024
TELA_ALTURA = 624
# tela dimensionada, mas podemos modificar para ver o q fica melhor

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

##IMAGENS_PODER = pygame.image.load(os.path.join('imagem', 'poder.png')) #deixei com um poder só, mas podemos adicionar mais
                                   
IMAGENS_CENARIO = [pygame.image.load(os.path.join('imagem', 'objeto1.png')),
                   pygame.image.load(os.path.join('imagem', 'objeto2.png')),
                   pygame.image.load(os.path.join('imagem', 'objeto3.png'))]#Variedade de objetos que irão compor o cenario

IMAGENS_BORDA = [[pygame.image.load(os.path.join('imagem', 'parede1_1.png')),
                 pygame.image.load(os.path.join('imagem', 'parede1_2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'parede2_1.png')),
                 pygame.image.load(os.path.join('imagem', 'parede2_2.png'))]]#2 tipos de paredes diferentes para as bordas em fazer flutando msm pra ficar mais facil, mas coloquei 3 para ter variedade

##IMAGENS_PORTA = [pygame.image.load(os.path.join('imagem', 'vilao1.png')),
##                 pygame.image.load(os.path.join('imagem', 'vilao2.png')),
##                 pygame.image.load(os.path.join('imagem', 'vilao3.png'))]#O que dará acesso a próxima sala

IMAGENS_BACKGROUND = pygame.image.load(os.path.join('imagem', 'bg.png')) #vou deixar só um fundo preto por enquanto, depois vejo se mudo isso de outro modo legal e iterativo que vi 

#Imagens carregadas, se formos adicionar som eles devem ser adicionados aqui dps

pygame.font.init() #Iniciei a fonte
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
FONTE_TIME = pygame.font.SysFont('arial', 50)
FONTE_VIDA = pygame.font.SysFont('arial',50)
FONTE_BG = pygame.font.SysFont('arial', 50)#vou tentar implementar dps um metodo iterativo pro BG
# deixei todas iguais para facilitar, mas depois podemos ir alterando

## Constantes do programa / Config padrão do jogo

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

class Heroi:
  IMGS = IMAGENS_HEROI
  VIDA_MAX = 3
  TEMPO_ANIMACAO = 5 #frames para mudar a imagem e criar uma animação

  def __init__(self, x, y, vida):
    self.x = x
    self.y = y
    self.vida = vida
    self.angulo = 0
    self.velocidade = 1
    self.cont_imagem = 0
    self.tempo = 0
    self.imagem = self.IMGS[0]

  def mover(self,move_left, move_right, move_down, move_up, contorno):

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
  
  def rotacionar(self,move_clockwise, move_counterclock):

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
    pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
    retangulo = self.imagem.get_rect(center=pos_centro_imagem)
    tela.blit(self.imagem_rot, retangulo.topleft)

    def get_mask(self):
      pygame.mask.from_surface(self.imagem_rot)

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

class Vilao:
  IMGSv = IMAGENS_VILAO
  TEMPO_ANIMACAOv = 5

  def __init__ (self, xv, yv, forca,number, angulo):
    self.number = number
    self.xv = xv
    self.yv = yv
    self.forca = 2
    self.cont_imagemv = 0
    self.tempo = 0
    self.angulov = angulo
    self.img_listav = self.IMGSv[self.number]
    self.imagemv = self.img_listav[0]


  def moverv(self,contorno,muda_dir):
    self.velocidade = 3
    aux_lista = []
    
    self.tempo += 1

    if self.cont_imagemv == self.TEMPO_ANIMACAOv:

      if self.yv <= contorno.topo.get_height() or muda_dir:
        self.angulov = random.randrange(180,360)

      if self.yv >= TELA_ALTURA - contorno.base.get_height() - self.imagemv.get_height() or muda_dir:
        self.angulov = random.randrange(0,180)

      if self.xv <= contorno.left.get_width() or muda_dir:
        aux_lista = [random.randrange(0,90), random.randrange(270,360)]
        self.angulov = aux_lista[random.randrange(0,1)]

      if self.xv >= TELA_LARGURA - contorno.right.get_width() - self.imagemv.get_width() or muda_dir:
        self.angulov = random.randrange(90,270)

    self.m = math.tan(math.radians(self.angulov)) #coeft. angular da reta

    if self.angulov > 0 and self.angulov <= 67.5:
      self.xv += self.velocidade
      self.yv -= (self.velocidade * self.m) #equaç. da reta

    if self.angulov > 67.5 and self.angulov <= 112.5:
      self.xv += 0
      self.yv -+ self.velocidade

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

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------
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

class Objetos:
  IMGo = IMAGENS_CENARIO

  def __init__ (self, xo, yo, anguloo):
    self.imagemo = self.IMGo[random.randrange(0,len(self.IMGo))]
    self.xo = xo
    self.yo = yo
    self.anguloo = anguloo
    self.imagem_roto = pygame.transform.rotate(self.imagemo, self.anguloo)

  def desenharo(self,tela):
    tela.blit(self.imagem_roto, (self.xo,self.yo))

    

  def colidir_o_H(self,heroi):
    pass

  def colidir_o_v(self,vilao):
    vilao_mask = vilao.get_maskv()
    obj_mask = pygame.mask.from_surface(self.imagem_roto)


    bateu_v = vilao_mask.overlap(obj_mask, (self.xo - round(vilao.xv),self.yo - round(vilao.yv)))#distancia)

    if bateu_v:
      return True
    else:
      return False
    
    
    
##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

##Códio principal do jogo

def geraro(contorno):
  number_of_O = random.randrange(1,4)
  objetos = []
  lista_angulo = [0, 0, 0, 180]
  for j in range(0,number_of_O):
    xo = random.randrange(contorno.left.get_width(),TELA_LARGURA - contorno.right.get_width() - 20)
    yo = random.randrange(contorno.topo.get_height(),TELA_ALTURA - contorno.base.get_height() - 20)
    anguloo = lista_angulo[random.randrange(0,3)]
    objeto = Objetos(xo,yo,anguloo)
    objetos.append(objeto)
  return objetos
    
  
def gerarv(contorno):
  number_of_V = random.randrange(1,5)
  viloes = []
  forca = 2
  for i in range(0,number_of_V):
    number = random.randrange(0,1)
    xv = random.randrange(contorno.left.get_width(),TELA_LARGURA - contorno.right.get_width() - 20)
    yv = random.randrange(contorno.topo.get_height(),TELA_ALTURA - contorno.base.get_height() - 20)
    angulov = random.randrange(0,360)
    vilao = Vilao(xv,yv,forca,number, angulov)
    viloes.append(vilao)
  return viloes


def desenhar_tela(tela, heroi, viloes, contorno, objetos):#, pontos):
  tela.blit(IMAGENS_BACKGROUND, (0,0))
  heroi.desenhar(tela)
  contorno.desenharc(tela)
  for v in viloes:
    v.desenharv(tela)
  for o in objetos:
    o.desenharo(tela)

##  texto = FONTE_PONTOS.render(f"Pontuação:{pontos}", 1, (255,255,255))
##  tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(),10))
  pygame.display.update()

def main():
  heroi = Heroi(230,350,3)
  number_of_v = random.randrange(0,4)
  contorno = Contorno()
  viloes = gerarv(contorno)
  objetos = geraro(contorno)
  trava_dir = False
  tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
  relogio = pygame.time.Clock()
  move_left = False
  move_right = False
  move_down = False
  move_up = False
  move_clockwise = False
  move_counterclock = False

  rodando =True
  while rodando:
    relogio.tick(30)

    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        rodando = False
        pygame.quit()
        quit()



      elif (evento.type == pygame.KEYDOWN):
        if(evento.key == pygame.K_RIGHT):
          move_right = True
        if(evento.key == pygame.K_LEFT) :
          move_left = True
        if(evento.key == pygame.K_DOWN) :
          move_down = True
        if(evento.key == pygame.K_UP) :
          move_up = True
        if(evento.key == pygame.K_c):
          move_clockwise = True
        if(evento.key == pygame.K_v):
          move_counterclock = True
      elif evento.type == pygame.KEYUP:
        if(evento.key == pygame.K_RIGHT):
          move_right = False
        if(evento.key == pygame.K_LEFT):
          move_left = False
        if(evento.key == pygame.K_DOWN):
          move_down = False
        if(evento.key == pygame.K_UP):
          move_up = False
        if(evento.key == pygame.K_c):
          move_clockwise = False
        if(evento.key == pygame.K_v):
          move_counterclock = False
          
    heroi.mover(move_left, move_right, move_down, move_up, contorno)
    heroi.rotacionar(move_clockwise, move_counterclock)
    for vilao in viloes:
      for obj in objetos:
        muda_dir = False
        if obj.colidir_o_v(vilao):
          muda_dir = True
        
      vilao.moverv(contorno,muda_dir)

    desenhar_tela(tela, heroi, viloes, contorno, objetos)#, pontos)  

main()




##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------


class Poder:
  pass
  
class Cenario:
  pass

class Nivel:
  pass

class BG:
  pass

class Usuario:
  pass




        
