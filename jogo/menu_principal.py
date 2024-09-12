import pygame
from classes import seta
branco = (255, 255, 255)
preto = (0,0,0)
personagens_escolhidos = []

def desenha_menu_escolhido(janela):
  clock = pygame.time.Clock()
  time = 0
  while True:
    clock.tick(1)
    time += 1
    if time == 2:
       break
    fundo = pygame.image.load("imagens/menu_escolhido.png")
    janela.blit(fundo, (0,0))
    pygame.display.flip()

def desenha_menu_principal(janela):
    fundo = pygame.image.load("imagens/Escolha seu personagem!.png")
    
    seta = pygame.image.load("imagens/seta_vermelha.png")
    seta = pygame.transform.scale_by(seta, 0.37)

    clock = pygame.time.Clock()

    pos_julian1  = (65,30)
    pos_marty1 = (725, 30)
    pos_gloria1 = (65, 360)
    pos_alex1 = (400, 360)
    pos_melman1 = (725, 360)
    pos_menu = pos_alex1
    fonte = pygame.font.Font("arquivos/fonte.ttf", 120)

    while True:

      clock.tick(120)
      
      text = fonte.render(f'{3 - len(personagens_escolhidos)}', True, (255,255,255))
  
      if len(personagens_escolhidos) == 3:
        return personagens_escolhidos
      
    
      for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
          pygame.quit()
        if evento.type == pygame.KEYDOWN:
          if evento.key == pygame.K_LEFT and pos_menu == pos_marty1:
            pos_menu = pos_julian1
          elif evento.key == pygame.K_LEFT and pos_menu == pos_melman1 :
            pos_menu = pos_alex1
          elif evento.key == pygame.K_LEFT and pos_menu == pos_alex1:
            pos_menu = pos_gloria1
                
          elif evento.key == pygame.K_RIGHT and pos_menu == pos_julian1:
            pos_menu = pos_marty1
          elif evento.key == pygame.K_RIGHT and pos_menu == pos_gloria1:
            pos_menu = pos_alex1
          elif evento.key == pygame.K_RIGHT and pos_menu == pos_alex1:
            pos_menu = pos_melman1

          elif evento.key == pygame.K_DOWN and pos_menu == pos_julian1:
            pos_menu = pos_gloria1
          elif evento.key == pygame.K_DOWN and pos_menu == pos_marty1:
            pos_menu = pos_melman1

          elif evento.key == pygame.K_UP and pos_menu == pos_gloria1:
            pos_menu = pos_julian1
          elif evento.key == pygame.K_UP and pos_menu == pos_melman1:
            pos_menu = pos_marty1
          elif evento.key == pygame.K_UP and pos_menu == pos_alex1:
            pos_menu = pos_julian1

          elif evento.key == pygame.K_z:
            if pos_menu == pos_julian1:
              if "julian" in personagens_escolhidos:
                desenha_menu_escolhido(janela)
              else:
                personagens_escolhidos.append("julian")
            
            elif pos_menu == pos_gloria1:
              if "gloria" in personagens_escolhidos:
                  desenha_menu_escolhido(janela)
              else:
                  personagens_escolhidos.append("gloria")
            
            elif pos_menu == pos_alex1:
              if "alex" in personagens_escolhidos:
                desenha_menu_escolhido(janela)
              else:
                personagens_escolhidos.append("alex")

            elif pos_menu == pos_melman1:
              if "melman" in personagens_escolhidos:
                desenha_menu_escolhido(janela)
              else:
                personagens_escolhidos.append("melman")

            elif pos_menu == pos_marty1:
              if "marty" in personagens_escolhidos:
                desenha_menu_escolhido(janela)
              else:
                personagens_escolhidos.append("marty")

      janela.blit(fundo, (0,0))
      janela.blit(seta, pos_menu)
      janela.blit(text, (475, 280))
      pygame.display.flip()

