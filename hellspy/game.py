import pygame
from pygame.locals import *
class personagem:
  def __init__(self,imagem,vida,posicao):
    self.imagem = imagem
    self.vida = vida
    self.posicao = posicao

  def setImage(self,imagem):
    self.imagem = imagem

class heroi(personagem):
  def __init__(self,imagem,vida,posicao,direcao):
    super().__init__(imagem,vida,posicao)
    self.direcao = direcao

class vilao(personagem):
  def __init__(self,imagem,vida,posicao,trajeto):
    super().__init__(imagem,vida,posicao)
    self.trajeto = trajeto

##class background:
####  def __init__(self,imagem):
####    
pygame.init()

width = 1000
high = 500
screen = pygame.display.set_mode((width,high))
pygame.display.set_caption("Hells.py")
x=250
y=250
speed = 10
heroi = pygame.image.load("imagem/quad.png")
#ballrect = ball.get_rect()
#speed2 = [1,1]
move_left = False
move_right = False
move_down = False
move_up = False
janela = True
    
while janela:
  pygame.time.delay(50)
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      janela = False

    elif (event.type == pygame.KEYDOWN):
      if(event.key == pygame.K_RIGHT):
        move_right = True
      if(event.key == pygame.K_LEFT) :
        move_left = True
      if(event.key == pygame.K_DOWN) :
        move_down = True
      if(event.key == pygame.K_UP) :
        move_up = True
    elif event.type == pygame.KEYUP:
      if(event.key == pygame.K_RIGHT):
        move_right = False
      if(event.key == pygame.K_LEFT):
        move_left = False
      if(event.key == pygame.K_DOWN):
        move_down = False
      if(event.key == pygame.K_UP):
        move_up = False
        
  screen.fill((0,0,0))
        
  screen.blit(heroi, (x,y))

  if(move_right) and x < (width-50):
    x += 10
  if(move_left) and x > 0:
    x -= 10
  if(move_down) and y < (high-50):
    y += 10
  if(move_up) and y > 0:
    y -= 10

  ##screen.blit(heroi, (x,y))
  
  pygame.display.update()

pygame.quit()
  
      
      


    #key = pygame.KEYDOWN
    #key = pygame.key.get_pressed()
  


##    ballrect = ballrect.move(speed2)
##    if ballrect.left < 0 or ballrect.right > 500:
##      speed[0]=-speed[0]
##    if ballrect.top < 0 or ballrect.bottom > 500:
##      speed[1]=-speed[1]
        

##  screen.fill((255,0,0))

##  pygame.display.flip()

        
