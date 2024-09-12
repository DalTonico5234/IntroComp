import pygame

class alex:

  def __init__(self):
    self.nome = "alex"
    self.escala = 0.5
    self.ataque = 225
    self.defesa = 100
    self.vida_max = 350
    self.vida = self.vida_max
    self.velocidade = 300
    self.string = "imagens/" + self.nome + "2.png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False
    self.habilide_ativa = False

  def mata(self):
    self.vivo = False
  
  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    if self.defesa_ativa:
      self.defesa /= 2
      self.defesa_ativa = False

  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def habilidade(self, players):
    self.habilide_ativa = True
    for player in players:
      player.ataque *= 2
    return players
  
  def interrompe_habilidade(self, players):
    if self.habilide_ativa:
      for player in players:
        player.ataque /= 2
      self.habilide_ativa = False
    return players


class gloria:

  def __init__(self):
    self.nome = "gloria"
    self.escala = 0.25
    self.ataque = 150
    self.defesa = 100
    self.vida_max = 350
    self.vida = self.vida_max
    self.velocidade = 200
    self.string = "imagens/"+ self.nome +"2.png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False
    self.habilide_ativa = False

  def mata(self):
    self.vivo = False
  
  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    self.defesa /= 2

  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def habilidade(self, inimigos):
    self.habilide_ativa = True
    for inimigo in inimigos:
      inimigo.defesa /= 2
    return inimigos
    
  def interrompe_habilidade(self, inimigos):
    if self.habilide_ativa:
      self.habilide_ativa = False
      for inimigo in inimigos:
        inimigo.defesa *= 2
    return inimigos
        

class julian:

  def __init__(self):
    self.nome = "julian"
    self.escala = 0.12
    self.ataque = 125
    self.defesa = 75
    self.vida_max = 250
    self.velocidade = 100
    self.vida = self.vida_max
    self.string = "imagens/" + self.nome + "2.png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False

  def mata(self):
    self.vivo = False
  
  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    self.defesa /= 2

  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def habilidade(self, players):
    for player in players:
      if player.nome == "julian":
        if player.vida + 50 <= player.vida_max: 
          player.vida += 50
        else:
          player.vida = player.vida_max 
      else:
        if player.vida + 25 <= player.vida_max: 
          player.vida += 25
        else:
          player.vida = player.vida_max   
    return players


class melman:

  def __init__(self):
    self.nome = "melman"
    self.escala = 0.2
    self.ataque = 150
    self.defesa = 125
    self.vida_max = 400
    self.velocidade = 400
    self.vida = self.vida_max
    self.string = "imagens/" + self.nome + "2.png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False
    self.habilide_ativa = False

  def mata(self):
    self.vivo = False
  
  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    self.defesa /= 2

  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def habilidade(self, players):
    self.habilide_ativa = True
    for player in players:
      player.defesa *= 2
    return players
  
  def interrompe_habilidade(self, players):
    if self.habilide_ativa:
      for player in players:
        player.defesa /= 2
      self.habilide_ativa = False
    return players
    

class marty:

  def __init__(self):
    self.nome = "marty"
    self.escala = 0.8
    self.ataque = 200
    self.defesa = 75
    self.vida_max = 300
    self.velocidade = 500
    self.vida = self.vida_max
    self.string = "imagens/" + self.nome + "2.png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False
    
  def mata(self):
    self.vivo = False
  
  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    self.defesa /= 2

  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def habilidade(self, inimigos, inimigos_vivos):
    for inimigo in inimigos:
      inimigo.recebe_ataque(self.ataque/1.5)
    return inimigos


class nana:

  def __init__(self):
    self.nome = "nana"
    self.escala = 0.75
    self.vida_max = 400
    self.vida = self.vida_max
    self.ataque = 275
    self.defesa = 100
    self.string = "imagens/" + self.nome + ".png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False

  def mata(self):
    self.vivo = False
    
  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    self.defesa /= 2

  
class mal:

  def __init__(self):
    self.nome = "chantel"
    self.escala = 0.39
    self.vida_max = 450
    self.vida = self.vida_max
    self.ataque = 225
    self.defesa = 125
    self.string = "imagens/" + self.nome + ".png"
    self.imagem = pygame.image.load(self.string)
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)
    self.vivo = True
    self.defesa_ativa = False

  def mata(self):
    self.vivo = False
    
  def recebe_ataque(self, ataque):
    dano = ataque*(50/(50 + self.defesa))
    self.vida -= dano

  def defende(self):
    self.defesa *= 2
    self.defesa_ativa = True

  def para_de_defender(self):
    self.defesa /= 2


class seta:
  def __init__(self, pos, cor):
    self.pos = pos
    self.escala = 0.22
    if cor == "vermelho":
      self.imagem = pygame.image.load("imagens/seta_vermelha.png")
    if cor == "azul":
      self.imagem = pygame.image.load("imagens/seta_azul2.png")
    if cor == "verde":
      self.imagem = pygame.image.load("imagens/seta_verde2.png")
    self.imagem = pygame.transform.scale_by(self.imagem, self.escala)