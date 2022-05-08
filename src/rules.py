import pygame

class Rules(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('assets/rules.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle