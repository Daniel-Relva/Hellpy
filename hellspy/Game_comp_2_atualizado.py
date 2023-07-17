import pygame
from pygame.locals import *
import os
import random
import math
## Bibliotecas necessárias para rodar o jogo.


TELA_LARGURA = 1000
TELA_ALTURA = 600
CONT = 0
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

IMAGEM_PODER = pygame.image.load(os.path.join('imagem', 'poder.png')) #deixei com um poder só, mas podemos adicionar mais
                                   
IMAGENS_CENARIO = [pygame.image.load(os.path.join('imagem', 'objeto1.png')),
                   pygame.image.load(os.path.join('imagem', 'objeto2.png')),
                   pygame.image.load(os.path.join('imagem', 'objeto3.png'))]#Variedade de objetos que irão compor o cenario

IMAGENS_BORDA = [[pygame.image.load(os.path.join('imagem', 'parede1_1.png')),
                 pygame.image.load(os.path.join('imagem', 'parede1_2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'parede2_1.png')),
                 pygame.image.load(os.path.join('imagem', 'parede2_2.png'))]]#2 tipos de paredes diferentes para as bordas em fazer flutando msm pra ficar mais facil, mas coloquei 3 para ter variedade

IMAGENS_PORTA = [[pygame.image.load(os.path.join('imagem', 'porta1_1.png')),
                 pygame.image.load(os.path.join('imagem', 'porta1_2.png'))],
                 [pygame.image.load(os.path.join('imagem', 'porta2_1.png')),#O que dará acesso a próxima sala
                  pygame.image.load(os.path.join('imagem', 'porta2_2.png'))]]

IMAGENS_VIDA = [pygame.image.load(os.path.join('imagem','vida1.png')),
                pygame.image.load(os.path.join('imagem','vida2.png'))]

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

  def mover(self,move_left, move_right, move_down, move_up, contorno, objetos, heroi):

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

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

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

##Funções auxiliares ao códio principal do jogo

def geraro(contorno):
  number_of_O = random.randrange(1,4)
  objetos = []
  lista_angulo = [0, 45, 90, 180]
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
    number = random.randrange(0,len(IMAGENS_VILAO))
    xv = random.randrange(contorno.left.get_width(),TELA_LARGURA - contorno.right.get_width() - 20)
    yv = random.randrange(contorno.topo.get_height(),TELA_ALTURA - contorno.base.get_height() - 20)
    angulov = random.randrange(0,360)
    vilao = Vilao(xv,yv,forca,number, angulov)
    viloes.append(vilao)
  return viloes


def desenhar_tela(tela, heroi, viloes, contorno, objetos, poderes, placar, portal, portal_gera):
  tela.blit(IMAGENS_BACKGROUND, (0,0))
  heroi.desenhar(tela)
  contorno.desenharc(tela)
  for v in viloes:
    v.desenharv(tela)
  for p in poderes:
    p.desenharp(tela)
  for o in objetos:
    o.desenharo(tela)
  placar.desenharplacar(tela)
  if portal_gera:
    portal.desenharport(tela)

  pygame.display.update()

##-------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------------

##Códio principal do jogo

def main():
  heroi = Heroi(230,350,3,0)
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
  colisao = 0
  bateu_dir = False
  bateu_esq = False
  bateu_baixo = False
  bateu_cima = False
  poderes = []
  pontos = 0
  tira_vida = False
  cont_coli = 0
  cont_coli2 = 0
  colisao_v_h = []
  colisao_v_p = []
  portal = Portal(random.randrange(0,TELA_LARGURA-100),random.randrange(0,TELA_ALTURA-100))
  portal_gera = False
  contador = 0

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
        if(evento.key == pygame.K_SPACE):
          poderes.append(Poder(heroi))
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
      
##----------------------------------------------------------------------------------------          
    for obj1 in objetos:
      if obj1.colidir_o_H(heroi):
        contador +=1
        print(colisao)
        if colisao == 0:
          colisao += 1                    ##Parte do código responsavél por não deixar o
          print(colisao)
          if move_right:                  ##heroi atravessar as paredes dos objetos        
            bateu_dir = True
            move_right = False
          if move_left:
            bateu_esq = True
            move_left = False
          if move_down:
            bateu_baixo = True
            move_down = False
          if move_up:
            bateu_cima = True
            move_up = False
        else:
          if bateu_dir:
            print('bateu dir')
            move_right = False
          if bateu_esq:
            print('bateu esq')
            move_left = False
          if bateu_baixo:
            print('bateu baixo')
            move_down = False
          if bateu_cima:
            print('bateu cima')
            move_up = False
      elif contador >= len(objetos):
        contador = 0
        colisao = 0
        bateu_dir = False
        bateu_esq = False
        bateu_baixo = False
        bateu_cima = False
##----------------------------------------------------------------------------------------

#mover as coisas e fazer as analises necessarias
    heroi.mover(move_left, move_right, move_down, move_up, contorno, objetos, heroi)
    heroi.rotacionar(move_clockwise, move_counterclock)

    remover_vilao = []
    remove_vilao2 = []
    remove_vilao3 = []
    for vilao in viloes:        
      for obj in objetos:
        muda_dir = False
        if obj.colidir_o_v(vilao):
          muda_dir = True                                                        

      muda_dir2 = False                                                            
      if heroi.colidir_h_v(vilao):                                                 
        if cont_coli == 0:
          cont_coli +=1
          colisao_v_h.append(vilao)
          muda_dir2 = True

      for poder1 in poderes:
        if poder1.colidir_v(vilao):
          if cont_coli2 ==0:
            colisao_v_p.append((vilao,poder1))
            cont_coli2 += 1
            if vilao.forca == 0:
              remover_vilao.append(vilao)

      vilao.moverv(contorno,muda_dir,muda_dir2)
##----------------------------------------------------------------------------------------

# Validação do que foi processado

    if len(remover_vilao)>0:
      pontos += len(remover_vilao)
      for vilao2 in remover_vilao:
        viloes.remove(vilao2)

    if len(colisao_v_h) > 0:
      remove_vilao2 = []
      for vilao4 in colisao_v_h:
        if not heroi.colidir_h_v(vilao4):
          remove_vilao2.append(vilao4)
          heroi.vida -=1
          cont_coli = 0

    if len(remove_vilao2) > 0:
      for vilao6 in remove_vilao2:
        colisao_v_h.remove(vilao6)

    if len(colisao_v_p) > 0:
      remove_vilao3 = []
      for v_p in colisao_v_p:
        if not v_p[1].colidir_v(v_p[0]):
          remove_vilao3.append(v_p)
          v_p[0].forca -=1
          cont_coli2 = 0

    if len(remove_vilao3) >0:
      for vilao7 in remove_vilao3:
        colisao_v_p.remove(vilao7)
      
## -------------------------------------------------------------------------------------------------------------------------------------
# atualizar as coisas
    cont = 0 
    for poder in poderes:
      poder.moverp()
      if poder.xp > TELA_LARGURA or poder.xp < 0 or poder.yp > TELA_ALTURA or poder.yp < 0:
        poderes.pop(cont)
      cont +=1

    placar = Placar(heroi.vida,pontos)

    if heroi.vida ==0:
        #termina o jogo e chama o ranking
        pass

    if len(viloes)==0:
      portal_gera = True

    if portal.colidir_portal_h(heroi):
      if portal_gera:
        print('entrou')
        if heroi.vida < 3:
          heroi.vida += 1
      #atualizar toda a pagina e se tiver coisa de nivel aumentar o nivel
      


    desenhar_tela(tela, heroi, viloes, contorno, objetos, poderes, placar, portal, portal_gera)  
##----------------------------------------------------------------------------------------
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




        
