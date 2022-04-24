import pygame

class Card(pygame.sprite.Sprite):

  def __init__(self, name=None, suit=None):
    super().__init__()
    self.name = name
    self.suit = suit

    if name == "Ace": 
      self.value = [1,11]
    elif name == "Jack" or name == "Queen" or name == "King":
      self.value = [10,10]
    else:
      self.value = [int(name), int(name)]
    
    pygame.image.load('assets/blank_card.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle
    self.rect.inflate_ip(-25, -25)
    self.rect.x = 10
    self.rect.y = 10