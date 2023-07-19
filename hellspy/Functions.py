import pygame
from pygame.locals import *
import os
import random
import math
from Personagens import *
from Cenarios import *

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

def desenhar_tela(tela, heroi, viloes, contorno, objetos, poderes, placar, portal, portal_gera,bk):
  bk.desenharbk(tela)
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

def iniciar_jogo(tela):
  fonte = pygame.font.SysFont('arial', 50)
  texto = 'PRESSIONE QUALQUER BOTÃO PARA INICIAR'
  mensagem = fonte.render(texto,False,'White')
  tela.blit(mensagem,(0,0))
  pygame.display.update()

def gerar_jogo():
  heroi = Heroi(230,350,3,0)
  contorno = Contorno()
  viloes = gerarv(contorno)
  objetos = geraro(contorno)
  
  return heroi, contorno, viloes, objetos

def teclado_input(evento,poderes,heroi):
  if evento.type == pygame.QUIT:
     rodando = False
     pygame.quit()
     quit()

  elif (evento.type == pygame.KEYDOWN):
    if(evento.key == pygame.K_d):
      move_right = True
    if(evento.key == pygame.K_a) :
      move_left = True 
    if(evento.key == pygame.K_s) :
      move_down = True
    if(evento.key == pygame.K_w) :
      move_up = True
    if(evento.key == pygame.K_LEFT):
      move_clockwise = True
    if(evento.key == pygame.K_RIGHT):
      move_counterclock = True
    if(evento.key == pygame.K_SPACE):
      poderes.append(Poder(heroi))
  elif evento.type == pygame.KEYUP:
    if(evento.key == pygame.K_d):
      move_right = False
    if(evento.key == pygame.K_a):
      move_left = False
    if(evento.key == pygame.K_s):
      move_down = False
    if(evento.key == pygame.K_w):
      move_up = False
    if(evento.key == pygame.K_LEFT):
        move_clockwise = False
    if(evento.key == pygame.K_RIGHT):
      move_counterclock = False

  move = [move_right,move_left,move_up,move_down]
  return rodando, move, poderes
  
def batida(obj1, objetos, move, heroi,contador,colisao, bateu):
  
  move_right,move_left,move_up,move_down = move
  bateu_baixo,bateu_esq,bateu_cima,bateu_dir = bateu
       
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
            move_right = False

          if bateu_esq:
            move_left = False

          if bateu_baixo:

            move_down = False
          if bateu_cima:

            move_up = False
  elif contador >= len(objetos):
    contador = 0
    colisao = 0
    bateu = [False,False,False,False]

  move = [move_right,move_left,move_up,move_down]
  bateu = [bateu_baixo,bateu_esq,bateu_cima,bateu_dir]
  return move, contador, colisao, bateu

   