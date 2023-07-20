import pygame
from pygame.locals import *
import os
import random
import math
from Personagens import *
from Cenarios import *
from Functions import *


def main():
  
  #Right, Left, Up, Down
  move = [False, False, False,False]
  #Clockwise, Counterclockwise
  spin = [False,False]
  bateu = [False,False,False,False]
  colisao = 0
  poderes = []
  pontos = 0
  ponto_maior = 0
  tira_vida = False
  cont_coli = 0
  cont_coli2 = 0
  colisao_v_h = []
  colisao_v_p = []
  portal = Portal(random.randrange(0,TELA_LARGURA-100),random.randrange(0,TELA_ALTURA-100))
  portal_gera = False
  contador = 0
  espera = True
  

  tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
  relogio = pygame.time.Clock()

  while espera:
    iniciar_jogo(tela)
    for evento in pygame.event.get():
      if (evento.type == pygame.KEYDOWN):

        espera = False
  
  jogando = True
  rodando = True
  while jogando:
    heroi, contorno, viloes, objetos = gerar_jogo()
    while rodando:
      relogio.tick(30)

      #---------
      # INPUT
      #--------
      for evento in pygame.event.get():
        rodando, move, poderes,spin = teclado_input(evento,poderes,heroi,move, spin,rodando)

      #---------
      #Colisão
      #--------
      for obj1 in objetos:
        move, contador, colisao, bateu =  batida(obj1, objetos, move, heroi,contador,colisao,bateu)


      #mover as coisas e fazer as analises necessarias
      heroi.mover(move, contorno, objetos, heroi)
      heroi.rotacionar(spin)

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
          break
        #atualizar toda a pagina e se tiver coisa de nivel aumentar o nivel
        


      desenhar_tela(tela, heroi, viloes, contorno, objetos, poderes, placar, portal, portal_gera)  
##----------------------------------------------------------------------------------------
main()








        
