import pygame, random
from random import randint
from classes import alex
from classes import julian
from classes import gloria
from classes import melman
from classes import marty
from classes import nana
from classes import mal
from classes import seta

def passa_vez(vez, players):
  if vez == 0 and players[1].vivo:
    vez = 1
  elif vez == 0 and players[2].vivo:
    vez = 2
  elif vez == 0:
    vez = 0
  
  elif vez == 1 and players[2].vivo:
    vez = 2
  elif vez == 1 and players[0].vivo:
    vez = 0
  elif vez == 1:
    vez = 1
    
  elif vez == 2 and players[0].vivo:
    vez = 0
  elif vez == 2 and players[1].vivo:
    vez = 1
  elif vez == 2:
    vez = 2
    
  return vez
    
    
def desenha_tudo (players, vez, big_fonte, small_fonte, texto_vida, inimigos, janela, fundo, seta1, seta_player, fim_de_turno):
    if players[vez].nome == "gloria":
      pronome = "DA"
    else:
      pronome = "DO"
    texto_vez = big_fonte.render("VEZ " + pronome + " " + players[vez].nome.upper(), True, (255,255,255))

    for n in range(3):
      texto_vida[n] = small_fonte.render((players[n].nome.upper() + " : " + f"{players[n].vida:.0f}" + " / " + f"{players[n].vida_max:.0f}"), True, (0, 0, 255))

    for n in range(3,5):
      texto_vida[n] = small_fonte.render((inimigos[n-3].nome.upper() + " : " + f"{inimigos[n-3].vida:.0f}" + " / " + f"{inimigos[n-3].vida_max:.0f}"), True, (255, 0, 0))

    if not(fim_de_turno):
      if vez == 0:
        seta_player.pos = (-30, 360)
      if vez == 1:
        seta_player.pos = (220, 470)
      if vez == 2:
        seta_player.pos = (-30, 570)

    # Atualização da tela conforme os personagens vivos, o texto e as setas
    janela.blit(fundo, (0,0))
    if players[0].vivo:
      janela.blit(players[0].imagem, (50, 280))
    if players[1].vivo:
      if players[1].nome == "gloria":
        janela.blit(players[1].imagem, (350, 443))
      elif players[1].nome == "alex":
        janela.blit(players[1].imagem, (290, 443))
      else: 
        janela.blit(players[1].imagem, (310, 443))
    if players[2].vivo:
      janela.blit(players[2].imagem, (50,520))
    if inimigos[0].vivo:
      janela.blit(inimigos[0].imagem, (790, 336))
    if inimigos[1].vivo:
      janela.blit(inimigos[1].imagem, (607, 461))
    janela.blit(texto_vez, (130, 20))
    h = 13
    for n in range(5):
      janela.blit(texto_vida[n], (680, h))
      h += 48
    janela.blit(seta1.imagem, seta1.pos)
    janela.blit(seta_player.imagem, seta_player.pos)


def realiza_batalha(janela, personagens_escolhidos):
  fundo = pygame.image.load("imagens/batalha.png")
  
  big_fonte = pygame.font.Font("arquivos/fonte.ttf", 55)
  small_fonte = pygame.font.Font("arquivos/fonte.ttf", 32)

  pos_menu1 = (-30, 80)
  pos_menu2 = (280, 80)
  pos_menu3 = (125, 145)
  
  pos_mal = (795, 265)
  pos_nana = (632, 390)

  pos_player1 = (-30, 360)
  pos_player2 = (220, 470)
  pos_player3 = (-30, 570)

  casa_do_caralho = (99999, 999999)

  seta1 = seta(pos_menu1, "verde")
  seta_player = seta((-30, 360), "azul")


  players = []
  
  for personagem in personagens_escolhidos:
    print(personagem)

    if personagem == "julian":
      players.append(julian())
    
    if personagem == "gloria":
      players.append(gloria())
    
    if personagem == "alex":
      players.append(alex())
    
    if personagem == "melman":
      players.append(melman())
    
    if personagem == "marty":
      players.append(marty())
      
  players = sorted(players, key = lambda p: -(p.velocidade))
  
  inimigos = []
  inimigos.append(mal())
  inimigos.append(nana())

  clock = pygame.time.Clock()

  players_vivos = 3
  inimigos_vivos = 2

  vez = 0

  jogados = 0

  jogo = True

  texto_vida = [small_fonte.render((players[0].nome.upper() + ":" + str(players[0].vida) + "/" + str(players[0].vida_max)), True, (255, 255, 255)), small_fonte.render((players[1].nome.upper() + ":" + str(players[1].vida) + "/" + str(players[1].vida_max)), True, (255, 255, 255)), small_fonte.render((players[2].nome.upper() + ":" + str(players[2].vida) + "/" + str(players[2].vida_max)), True, (255, 255, 255)), small_fonte.render((inimigos[0].nome.upper() + ":" + str(inimigos[0].vida) + "/" + str(inimigos[0].vida_max)), True, (255, 255, 255)), small_fonte.render((inimigos[1].nome.upper() + ":" + str(inimigos[1].vida) + "/" + str(inimigos[1].vida_max)), True, (255, 255, 255))]

  while jogo:

    clock.tick(120)
  
    for inimigo in inimigos:
      if inimigo.vida < 0:
        inimigo.vida = 0
      if inimigo.vida == 0 and inimigo.vivo:
        inimigos_vivos -= 1
        inimigo.mata()
    if inimigos_vivos == 0:
      return "aniquilação"
  
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
      if evento.type == pygame.KEYDOWN:
        # Menu de seleção
        if evento.key == pygame.K_RIGHT and seta1.pos == pos_menu1:
          seta1.pos = pos_menu2
        elif evento.key == pygame.K_RIGHT and seta1.pos == pos_menu3:
          seta1.pos = pos_menu2
        elif evento.key == pygame.K_LEFT and seta1.pos == pos_menu2:
          seta1.pos = pos_menu1
        elif evento.key == pygame.K_DOWN and (seta1.pos == pos_menu1 or seta1.pos == pos_menu2):
          seta1.pos = pos_menu3
        elif (evento.key == pygame.K_UP or evento.key == pygame.K_LEFT) and seta1.pos == pos_menu3:
          seta1.pos = pos_menu1
        
        # Menu de inimigos
        elif evento.key == pygame.K_z and seta1.pos == pos_menu1 and inimigos[0].vivo:
          seta1 = seta(pos_mal, "vermelho")
        elif evento.key == pygame.K_z and seta1.pos == pos_menu1:
          seta1 = seta(pos_nana, "vermelho")
        elif (evento.key == pygame.K_DOWN or evento.key == pygame.K_LEFT) and seta1.pos == pos_mal and inimigos[1].vivo:
          seta1.pos = pos_nana
        elif (evento.key == pygame.K_UP or evento.key == pygame.K_RIGHT) and seta1.pos == pos_nana and inimigos[0].vivo:
          seta1.pos = pos_mal
          
        #Voltando para o menu de seleção
        elif evento.key == pygame.K_x and (seta1.pos == pos_mal or seta1.pos == pos_nana):
          seta1 = seta(pos_menu1, "verde")
          
        # Selecionando o ataque
        elif evento.key == pygame.K_z and seta1.pos == pos_mal:
          inimigos[0].recebe_ataque(players[vez].ataque)
          vez = passa_vez(vez, players)
          seta1 = seta(pos_menu1, "verde")
          jogados += 1
          for inimigo in inimigos:
            if inimigo.vida < 0:
              inimigo.vida = 0
            if inimigo.vida == 0 and inimigo.vivo:
              inimigos_vivos -= 1
              inimigo.mata()
          if inimigos_vivos == 0:
            return "aniquilação"
        elif evento.key == pygame.K_z and seta1.pos == pos_nana:
          inimigos[1].recebe_ataque(players[vez].ataque)
          vez = passa_vez(vez, players)
          seta1 = seta(pos_menu1, "verde")
          jogados += 1
          for inimigo in inimigos:
            if inimigo.vida < 0:
              inimigo.vida = 0
            if inimigo.vida == 0 and inimigo.vivo:
              inimigos_vivos -= 1
              inimigo.mata()
          if inimigos_vivos == 0:
            return "aniquilação"
          
        # Selecionando a defesa
        elif evento.key == pygame.K_z and seta1.pos == pos_menu2:
          players[vez].defende()
          vez = passa_vez(vez, players)
          jogados += 1
          
        # Selecionando a habilidade
        elif evento.key == pygame.K_z and seta1.pos == pos_menu3:
          if players[vez].nome == "alex" or players[vez].nome == "julian" or players[vez].nome == "melman":
            players = players[vez].habilidade(players)
          elif players[vez].nome == "gloria":
            inimigos = players[vez].habilidade(inimigos)
          elif players[vez].nome == "marty":
            inimigos = players[vez].habilidade(inimigos, inimigos_vivos)
          vez = passa_vez(vez, players)
          jogados += 1
          for inimigo in inimigos:
            if inimigo.vida < 0:
              inimigo.vida = 0
            if inimigo.vida == 0 and inimigo.vivo:
              inimigos_vivos -= 1
              inimigo.mata()
          if inimigos_vivos == 0:
            return "aniquilação"
            
    
    # Fim do turno 
    if jogados == players_vivos:
      fim_de_turno = True
      jogados = 0
    else:
      fim_de_turno = False
    
    if fim_de_turno:
      for inimigo in inimigos:
        if inimigo.vivo:
          # Reinicia o estado da defesa do inimigo
          inimigo.para_de_defender()
          # Define se irá atacar ou defender
          escolha_inimigo = randint(0,1)
          vivos = []
          # Inimigo atacando
          if escolha_inimigo:
            if players[0].vivo:
              vivos.append(0)
            if players[1].vivo:
              vivos.append(1)
            if players[2].vivo:
              vivos.append(2)
            if players_vivos == 0:
              return "morte"
            atacado = random.choice(vivos)
            players[atacado].recebe_ataque(inimigo.ataque)
            if players[atacado].vida < 0:
              players[atacado].vida = 0
            if players[atacado].vida == 0:
              players[atacado].mata()
              players_vivos -= 1
            if players_vivos == 0:
              return "morte"
          # Inimigo defendendo
          else:
            inimigo.defende()
            atacado = 3
          clock2 = pygame.time.Clock()
          tempo = 0
          # Animação de inimigos
          while tempo <= 2:
            clock2.tick(1)
            tempo += 1
            if inimigo.nome == "chantel":
              seta1 = seta(pos_mal, "vermelho")
            elif inimigo.nome == "nana":
              seta1 = seta(pos_nana, "vermelho")
            if escolha_inimigo:
              if atacado == 0:
                seta_player.pos = pos_player1
              elif atacado == 1:
                seta_player.pos = pos_player2
              elif atacado == 2:
                seta_player.pos = pos_player3
              elif atacado == 3:
                seta_player.pos = casa_do_caralho
            desenha_tudo (players, vez, big_fonte, small_fonte, texto_vida, inimigos, janela, fundo, seta1, seta_player, fim_de_turno)
            pygame.display.flip()
      seta1 = seta(pos_menu1, "verde")
      # Reinicia o turno
      if players[0].vivo:
        vez = 0
      elif players[1].vivo:
        vez = 1
      elif players[2].vivo:
        vez = 2
      # Reinicia as habilidades necessárias e o estado de defesa
      for player in players:
        if player.nome == "alex" or player.nome == "melman":
          players = player.interrompe_habilidade(players)
        elif player.nome == "gloria":
          inimigos = player.interrompe_habilidade(inimigos)
        player.para_de_defender()
        
    desenha_tudo (players, vez, big_fonte, small_fonte, texto_vida, inimigos, janela, fundo, seta1, seta_player, fim_de_turno)

    pygame.display.flip()