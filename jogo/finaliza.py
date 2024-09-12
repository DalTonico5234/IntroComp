import pygame

def perdeu(janela):
  fundo = pygame.image.load("imagens/perdeu.png")

  clock = pygame.time.Clock()

  timer = 0

  janela.blit(fundo, (0,0))
  pygame.display.flip()

  while True:
    clock.tick(2)
    timer += 1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
          pygame.quit()

    if timer == 8:
      pygame.quit()

def ganhou(janela):
  fundo = pygame.image.load("imagens/ganhou.png")

  clock = pygame.time.Clock()

  timer = 0

  janela.blit(fundo, (0,0))
  pygame.display.flip()

  while True:
    clock.tick(2)
    timer += 1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
          pygame.quit()

    if timer == 8:
      return 0