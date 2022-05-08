import pygame

class Button(pygame.sprite.Sprite):
  '''
    (D)eal (H)it (S)tand 
    (I10)(I100)IncreaseBet (D10)(D100)DecreaseBet
    (Do)ubleUp (Q)uadUp (O)ctUp (R)ules (E)xit
  '''
  D_pos = [0,0]
  Re_pos = [0,0]
  H_pos = [0,0]
  S_pos = [0,0]
  Sp_pos = [0,0]
  I1_pos = [0,0]
  I10_pos = [0,0]
  I100_pos = [0,0]
  D1_pos = [0,0]
  D10_pos = [0,0]
  D100_pos = [0,0]
  Do_pos = [0,0]
  Q_pos = [0,0]
  O_pos = [0,0]
  R_pos = [0,0]
  E_pos = [0,0]
  
  def __init__(self, pos = [0,0], message = "", t_color = (0,0,0), bg_color = (0,0,0)):
    '''
      Creates Button Object and pygame Surface for the Button object.
      pos [(int)x, (int)y]: x and y values of the top left corner of the object on screen
      message (str): Text displayed on the button in game
      t_color ((int)R, (int)G, (int)B): RGB values of the text color for this button
      bg_color ((int)R, (int)G, (int)B): RGB values of the background color for this button

      return: None
    '''
    super().__init__()
    #self.image = pygame.image.load('assets/button.png').convert_alpha()
    #self.rect = self.image.get_rect()  # rectangle
    #self.rect.inflate_ip(-1, -1)
    #self.rect.x = pos[0]
    #self.rect.y = pos[1]
    self.pos = pos
    myfont = pygame.font.SysFont(None, 50)
    self.text = message
    self.message = myfont.render(message, True, t_color, bg_color)
    self.rect = self.message.get_rect()  # rectangle
    self.rect.x = pos[0]
    self.rect.y = pos[1]