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

    if suit[0] == "H":
      self.t_color = (255,0,0)
    elif suit[0] == "C":
      self.t_color = (0,150,0)
    elif suit[0] == "S":
      self.t_color = (0,0,0)
    else:
      self.t_color = (0,0,255)
    
    myfont = pygame.font.SysFont(None, 70)
    if self.name[0] == '1':
      self.message = myfont.render(f"{self.name}", True, self.t_color, (255,255,255))
    else:
      self.message = myfont.render(f"{self.name[0]}", True, self.t_color, (255,255,255))

  def __str__(self):
    return f"{str(self.name)} of {str(self.suit)}"

  def printCard(self):
    print(str(self))