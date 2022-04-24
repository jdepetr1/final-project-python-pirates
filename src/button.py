import pygame

class Button(pygame.sprite.Sprite):
  #(D)eal (Re)bet (H)it (S)tand (Do)ubleUp (Q)uadUp (O)ctUp (R)ules (E)xit
  
  def __init__(self, func = "D"):
    super().__init__()
    pygame.image.load('assets/button.png').convert_alpha()
    self.rect = self.image.get_rect()  # rectangle
    self.rect.inflate_ip(-25, -25)
    self.rect.x = 10
    self.rect.y = 10
    self.function = func

  def changeFunction(self, func = "D"):
    '''
      Changes the function of a specific button object
      func (str): representation of new button function
      return: None
    '''
    self.function = func
    
  def buttonFunction(self):
    '''
      returns string representation of button function
      inputs: None
      return: self.function (str)
    '''
    return self.function
