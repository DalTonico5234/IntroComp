import pygame
from menu_principal import desenha_menu_principal
from finaliza import perdeu
from finaliza import ganhou
from batalha import realiza_batalha

# Inicializar o Pygame
pygame.init()
pygame.mixer.music.load("arquivos/musica.mp3")
pygame.mixer.music.play(-1)

# Inicializa a janela do jogo
janela = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Madagascar.py')
janela.fill((0,0,0))

# Menu principal
personagens_escolhidos = desenha_menu_principal(janela)

# Menu de batalha
resultado = realiza_batalha(janela, personagens_escolhidos)

# Menu de encerramento
if resultado == "morte":
    perdeu(janela)
elif resultado == "aniquilação":
    ganhou(janela)

#fechar o jogo
pygame.quit()