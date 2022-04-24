import pygame

class Background(pygame.sprite.Sprite):
  #Function Strings:
  #(D)eal (Re)bet (H)it (S)tand (Do)ubleUp (Q)uadUp (O)ctUp (R)ules (E)xit
  
  def __init__(self):
    super().__init__()
    pygame.image.load('assets/background.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle
    self.rect.inflate_ip(-25, -25)
    self.rect.x = 10
    self.rect.y = 10