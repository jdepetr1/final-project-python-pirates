import pygame

class Chip(pygame.sprite.Sprite):

  def __init__(self, value = 1):
    super().__init__()
    self.value = value
    
    pygame.image.load('assets/chip.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle
    self.rect.inflate_ip(-25, -25)
    self.rect.x = 10
    self.rect.y = 10