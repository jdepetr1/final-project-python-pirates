import sys
import pygame
from src import player
from src import dealer
from src import deck
from src import button
from src import rules


class Controller:
  
  def __init__(self):
    '''
      Sets up initial pygame and general game data, gets dimensions of the user's pygame window, and initializes the state of the program.

      return: None
    '''
    pygame.init()
    pygame.font.init()
    self.screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)
    self.width = self.screen.get_width()
    self.height = self.screen.get_height()
    self.player = player.Player()
    self.dealer = dealer.Dealer()
    self.myfont = pygame.font.SysFont(None, 50)
    self.makeButtons(self.width, self.height)
    self.bg = pygame.image.load('assets/background.png').convert_alpha()
    self.bg = pygame.transform.scale(self.bg, [self.width, self.height])
    self.bet = 10
    self.card_off = 20
    self.all_buttons = pygame.sprite.Group()
    self.all_buttons.add(self.dealB, self.hitB, self.standB, self.inc10B, self.inc100B, self.dec10B, self.dec100B, self.doubleB, self.quadB, self.octB, self.rulesB, self.exitB)
    self.rule  = rules.Rules()
    self.rule.image = pygame.transform.scale(self.rule.image, [self.rule.rect.width, self.rule.rect.height])
    self.card_back = self.myfont.render("X", True, (198,33,50), (255,33,50))
    self.bet_S = self.myfont.render(f"Bet: {self.bet}", True, (0,0,0), (255,255,255))
    self.state = "PREGAME"
    
    
    
  def mainloop(self):
    '''
      Controls which state Jack-Black-Jake is in at specific times dependent on self.state

      return: None
    '''
    while True:
      
      if self.state == "PREGAME":
        self.menuloop()
      elif self.state == "PLAYING":
        self.gameloop()
      elif self.state == "RULES":
        self.rulesloop()
      elif self.state == "SHOWDOWN":
        self.showdownloop()
      elif self.state == "WIN":
        self.winloop()
      elif self.state == "LOSE":
        self.loseloop()
      elif self.state == "PUSH":
        self.pushloop()
      elif self.state == "EXIT":
        self.exitloop()

  def menuloop(self):
    '''
      Controls the display of all Button objects in the menu, when the player is still placing their bet.

      return: None
    '''
    self.bet = 10
    self.deck = deck.Deck()
    print("-----------------New Hand-----------------")
      #event loop
    while self.state == "PREGAME":
      self.screen.blit(self.bg, (0, 0))
      self.screen.blit(self.money.message, self.money.pos)
      self.screen.blit(self.dealB.message, self.dealB.pos)
      self.screen.blit(self.inc10B.message, self.inc10B.pos)
      self.screen.blit(self.inc100B.message, self.inc100B.pos)
      self.screen.blit(self.dec10B.message, self.dec10B.pos)
      self.screen.blit(self.dec100B.message, self.dec100B.pos)
      self.screen.blit(self.rulesB.message, self.rulesB.pos)
      self.screen.blit(self.exitB.message, self.exitB.pos)
      self.bet_S = self.myfont.render(f"Bet: {self.bet}", True, (0,0,0), (255,255,255))
      self.bet_S = pygame.transform.scale(self.bet_S, [self.width/5,self.height/10])
      self.screen.blit(self.bet_S, [2*self.width/5,11*self.height/18])
      ev = pygame.event.get()
      
      for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          clicked_sprites = [s for s in self.all_buttons if s.rect.collidepoint(pos)]
          if self.dealB in clicked_sprites:
            self.state = "PLAYING"
            if int(self.money.text) < self.bet:
              self.bet = int(self.money.text)
            self.money.text = str(int(self.money.text)-self.bet)
            self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
            self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])
          elif self.inc10B in clicked_sprites:
            self.bet += 10
          elif self.inc100B in clicked_sprites:
            self.bet += 100
          elif self.dec10B in clicked_sprites:
            if self.bet >= 20:
              self.bet -= 10
            else:
              self.bet = 10
          elif self.dec100B in clicked_sprites:
            if self.bet >= 110:
              self.bet -= 100
            else:
              self.bet = 10
          elif self.rulesB in clicked_sprites:
            self.state = "RULES"
          elif self.exitB in clicked_sprites:
            self.state = "EXIT"
            
      pygame.display.flip()
      
  def gameloop(self):
    '''
      Controls the display of all Button objects while the game is being played, when the player is deciding what action to take with their cards.

      return: None
    '''
    self.player.clearHand()
    self.dealer.clearHand()
    self.deck.shuffle()
    
    for _ in range(3):
      self.player.addCard2Hand(self.deck)
      self.dealer.addCard2Hand(self.deck)
    p_total = self.player.handTotal()
    d_total = self.dealer.handTotal()
    self.dealer.printHand()
    if (p_total[1] == 31 and len(self.player.cards) == 3) or (d_total[1] == 31 and len(self.dealer.cards) == 3) or (p_total[0] > 31):
      self.state = "SHOWDOWN"
      
      
    HIT = 0
    DOUBLE = 0
    QUAD = 0
    OCT = 0
    while self.state == "PLAYING":
      self.screen.blit(self.bg, (0, 0))
      if not DOUBLE == 1:
        self.screen.blit(self.hitB.message, self.hitB.pos)
      self.screen.blit(self.money.message, self.money.pos)
      self.screen.blit(self.standB.message, self.standB.pos)
      for i in range(0, len(self.player.cards)):
        self.screen.blit(self.player.cards[i].message, [(i+1)*self.width/(len(self.player.cards)+1),3*self.height/4])
      for i in range(0, len(self.dealer.cards)):
        if i < 2:
          self.screen.blit(self.card_back, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
        else:
          self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
        
      if DOUBLE == 0 and HIT == 0 and (int(self.money.text) >= self.bet):
        self.screen.blit(self.doubleB.message, self.doubleB.pos)
      if DOUBLE == 1 and QUAD == 0 and (int(self.money.text) >= self.bet):
        self.screen.blit(self.quadB.message, self.quadB.pos)
      if QUAD == 1 and OCT == 0 and (int(self.money.text) >= self.bet):
        self.screen.blit(self.octB.message, self.octB.pos)

      ev = pygame.event.get()
      for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          clicked_sprites = [s for s in self.all_buttons if s.rect.collidepoint(pos)]
          if self.hitB in clicked_sprites:
            self.player.addCard2Hand(self.deck)
            HIT += 1
          elif self.standB in clicked_sprites:
            self.state = "SHOWDOWN"
            for i in range(0, len(self.dealer.cards)):
              self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
            pygame.display.flip()
            pygame.time.wait(1000)
          elif self.doubleB in clicked_sprites:
            DOUBLE = 1
            self.player.addCard2Hand(self.deck)
            self.money.text = str(int(self.money.text)-self.bet)
            self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
            self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])
            self.bet *= 2
          elif self.quadB in clicked_sprites:
            QUAD = 1
            self.player.addCard2Hand(self.deck)
            self.money.text = str(int(self.money.text)-self.bet)
            self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
            self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])
            self.bet *= 2
          elif self.octB in clicked_sprites:
            OCT = 1
            self.player.addCard2Hand(self.deck)
            self.money.text = str(int(self.money.text)-self.bet)
            self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
            self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])
            self.bet *= 2
            
      pygame.display.flip()
      
  def rulesloop(self):
    '''
      Displays the rules of the game for the player.

      return: None
    '''
    while self.state == "RULES":
      self.screen.blit(self.bg, (0, 0))
      self.screen.blit(self.rule.image, (self.width/8,self.height/10))
      self.screen.blit(self.rulesB.message, self.rulesB.pos)
      ev = pygame.event.get()
      for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          clicked_sprites = [s for s in self.all_buttons if s.rect.collidepoint(pos)]
          if self.rulesB in clicked_sprites:
            self.state = "PREGAME"
      pygame.display.flip()
                       
  def exitloop(self):
    '''
      Closes the program and creates a text file containing the amount of money the player cashed out of the table with.

      return: None
    '''
    fp = open("cash_out.txt", "w")
    fp.write(f"You have cashed out of the Jack-Black-Jack table with ${self.money.text}.")
    fp.close()
    pygame.quit()
    sys.exit()

  def showdownloop(self):
    '''
      Takes care of all dealer decisions and the general logic of the game. Also blits cards in player's hand and dealer's hand as they are added.

      return: None
    '''
    
    while self.state == "SHOWDOWN":
      self.screen.blit(self.bg, (0, 0))
      for i in range(0, len(self.player.cards)):
        self.screen.blit(self.player.cards[i].message, [(i+1)*self.width/(len(self.player.cards)+1),3*self.height/4])
      for i in range(0, len(self.dealer.cards)):
        self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
      p_total = self.player.handTotal()
      d_total = self.dealer.handTotal()

      if d_total[1] == 31 and len(self.dealer.cards) == 3:
        self.state = "LOSE"
      elif p_total[0] > 31:
        self.state = "LOSE"
      elif d_total[0] > 31:
        self.state = "WIN"
      else:
        if d_total[0] == d_total[1]:
          if p_total[0] == p_total[1]:
            if d_total[0] >= 27:
              if p_total[0] == d_total[0]:
                self.state = "PUSH"
              elif p_total[0] < d_total[0]:
                self.state = "LOSE"
              elif p_total[0] > d_total[0]:
                self.state = "WIN"
            else:
              self.dealer.addCard2Hand(self.deck)
          else:
            if d_total[0] >= 27:
              if p_total[0] == d_total[0] or p_total[1] == d_total[0]:
                self.state = "PUSH"
              elif p_total[1] < d_total[0]:
                self.state = "LOSE"
              elif p_total[0] > d_total[0] or p_total[1] > d_total[0]:
                self.state = "WIN"
            else:
              self.dealer.addCard2Hand(self.deck)
        else:
          if p_total[0] == p_total[1]:
            if d_total[1] >= 27:
              if p_total[0] == d_total[0] or p_total[0] == d_total[1]:
                self.state = "PUSH"
              elif p_total[0] < d_total[1]:
                self.state = "LOSE"
              elif p_total[0] > d_total[0]:
                if d_total[1] > 31:
                  self.state = "WIN"
                else:
                  if p_total[0] > d_total[1]:
                    self.state = "WIN"
                  else:
                    self.state = "LOSE"
            else:
              self.dealer.addCard2Hand(self.deck)
          else:
            if d_total[1] > 31:
              if d_total[0] >= 27:
                if p_total[1] > 31:
                  if p_total[0] == d_total[0]:
                    self.state = "PUSH"
                  elif p_total[0] < d_total[0]:
                    self.state = "LOSE"
                  elif p_total[0] > d_total[0]:
                    self.state = "WIN"
                else:
                  if p_total[1] == d_total[0]:
                    self.state = "PUSH"
                  elif p_total[1] < d_total[0]:
                    self.state = "LOSE"
                  elif p_total[1] > d_total[0]:
                    self.state = "WIN"
              else:
                self.dealer.addCard2Hand(self.deck)
            elif d_total[1] >= 27:
              if p_total[1] > 31:
                if p_total[0] == d_total[1]:
                  self.state = "PUSH"
                elif p_total[0] < d_total[1]:
                  self.state = "LOSE"
                elif p_total[0] > d_total[1]:
                  self.state = "WIN"
              else:
                if p_total[1] == d_total[1]:
                  self.state = "PUSH"
                elif p_total[1] < d_total[1]:
                  self.state = "LOSE"
                elif p_total[1] > d_total[1]:
                  self.state = "WIN"
            else:
              self.dealer.addCard2Hand(self.deck)
      self.screen.blit(self.bg, (0,0))
      self.screen.blit(self.money.message, self.money.pos)
      for i in range(0, len(self.player.cards)):
        self.screen.blit(self.player.cards[i].message, [(i+1)*self.width/(len(self.player.cards)+1),3*self.height/4])
      for i in range(0, len(self.dealer.cards)):
        self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
      
      pygame.display.flip()
      pygame.time.wait(1000)

  def winloop(self):
    '''
      Blits winning message and adjusts remaining money accordingly when the player beats the dealer

      return: None
    '''
    p_total = self.player.handTotal()
    if p_total[1] == 31 and len(self.player.cards) == 3:
      self.money.text = str(int(int(self.money.text)+3.5*self.bet))
      self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
      self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])
    else:
      self.money.text = str(int(self.money.text)+2*self.bet)
      self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
      self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])

    while self.state == "WIN":
      self.screen.blit(self.bg, (0,0))
      self.screen.blit(self.money.message, self.money.pos)
      for i in range(0, len(self.player.cards)):
        self.screen.blit(self.player.cards[i].message, [(i+1)*self.width/(len(self.player.cards)+1),3*self.height/4])
      for i in range(0, len(self.dealer.cards)):
        self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
      if p_total[1] == 31 and len(self.player.cards) == 3:
        self.screen.blit(self.JBJ_S.message, self.JBJ_S.pos)
      else:
        self.screen.blit(self.win_S.message, self.win_S.pos)
      pygame.display.flip()
      pygame.time.wait(2000)
      self.state = "PREGAME"

  def loseloop(self):
    '''
      Blits losing message and adjusts remaining money accordingly when the player loses to the dealer

      return: None
    '''
    while self.state == "LOSE":
      self.screen.blit(self.bg, (0,0))
      self.screen.blit(self.money.message, self.money.pos)
      for i in range(0, len(self.player.cards)):
        self.screen.blit(self.player.cards[i].message, [(i+1)*self.width/(len(self.player.cards)+1),3*self.height/4])
      for i in range(0, len(self.dealer.cards)):
        self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
      self.screen.blit(self.lose_S.message, self.lose_S.pos)
      pygame.display.flip()
      pygame.time.wait(2000)
      self.state = "PREGAME"

  def pushloop(self):
    '''
      Blits 'push' message and adjusts remaining money accordingly when the player ties with the dealer

      return: None
    '''
    self.money.text = str(int(self.money.text)+self.bet)
    self.money.message = self.myfont.render(self.money.text, True, (0,0,0), (255,255,255))
    while self.state == "PUSH":
      self.screen.blit(self.bg, (0,0))
      self.screen.blit(self.money.message, self.money.pos)
      for i in range(0, len(self.player.cards)):
        self.screen.blit(self.player.cards[i].message, [(i+1)*self.width/(len(self.player.cards)+1),3*self.height/4])
      for i in range(0, len(self.dealer.cards)):
        self.screen.blit(self.dealer.cards[i].message, [(i+1)*self.width/(len(self.dealer.cards)+1),self.height/4])
      self.screen.blit(self.push_S.message, self.push_S.pos)
      pygame.display.flip()
      pygame.time.wait(2000)
      self.state = "PREGAME"

  def makeButtons(self, s_width, s_height):
    '''
      Creates all Button objects used in Jack-Black-Jack
      s_width (int): Screen Width
      s_height (int): Screen Height

      return: None
    '''
    _BLACK_ = (0,0,0)
    _BLUE_ = (0,0,255)
    _GREEN_ = (0,255,0)
    _CYAN_ = (0,255,255)
    _RED_ = (255,0,0)
    _PURPLE_ = (255,0,255)
    _YELLOW_ = (255,255,0)
    _WHITE_ = (255,255,255)
    
    self.dealB = button.Button([4*s_width/9,7*s_height/8], "Deal", _BLACK_, _BLUE_)
    self.dealB.message = pygame.transform.scale(self.dealB.message, [self.width/10, self.height/10])
    
    self.rebetB = button.Button([2*s_width/3,7*s_height/8], "Re-Bet", _BLACK_, _RED_)
    self.rebetB.message = pygame.transform.scale(self.rebetB.message, [self.width/10, self.height/10])
    
    self.hitB = button.Button([s_width/3,7*s_height/8], "Hit", _BLACK_, _PURPLE_)
    self.hitB.message = pygame.transform.scale(self.hitB.message, [self.width/10, self.height/10])
    
    self.standB = button.Button([s_width/2,7*s_height/8], "Stand", _BLACK_, _GREEN_)
    self.standB.message = pygame.transform.scale(self.standB.message, [self.width/10, self.height/10])
    
    self.inc10B = button.Button([4*s_width/10, 3*s_height/4], "+10", _BLACK_, _CYAN_)
    self.inc10B.message = pygame.transform.scale(self.inc10B.message, [self.width/15, self.height/15])
    
    self.inc100B = button.Button([3*s_width/10, 3*s_height/4], "+100", _BLACK_, _CYAN_)
    self.inc100B.message = pygame.transform.scale(self.inc100B.message, [self.width/15, self.height/15])

    self.dec10B = button.Button([5*s_width/10, 3*s_height/4], "-10", _BLACK_, _CYAN_)
    self.dec10B.message = pygame.transform.scale(self.dec10B.message, [self.width/15, self.height/15])
    
    self.dec100B = button.Button([6*s_width/10, 3*s_height/4], "-100", _BLACK_, _CYAN_)
    self.dec100B.message = pygame.transform.scale(self.dec100B.message, [self.width/15, self.height/15])
    
    self.doubleB = button.Button([0,s_height/5], "Double", _BLACK_, _YELLOW_)
    self.doubleB.message = pygame.transform.scale(self.doubleB.message, [self.width/10, self.height/10])
    
    self.quadB = button.Button([0,2*s_height/5], "Quad-Up", _BLACK_, _GREEN_)
    self.quadB.message = pygame.transform.scale(self.quadB.message, [self.width/10, self.height/10])
    
    self.octB = button.Button([0,3*s_height/5], "Oct-Up", _BLACK_, _CYAN_)
    self.octB.message = pygame.transform.scale(self.octB.message, [self.width/10, self.height/10])
    
    self.rulesB = button.Button([7*s_width/8,s_height/8], "Rules", _BLACK_, _GREEN_)
    self.rulesB.message = pygame.transform.scale(self.rulesB.message, [self.width/10, self.height/10])
    
    self.exitB = button.Button([3*s_width/4,7*s_height/8], "Cash Out", _BLACK_, _WHITE_)
    self.exitB.message = pygame.transform.scale(self.exitB.message, [self.width/5, self.height/10])

    self.money = button.Button([0,s_height/8], "5000", _BLACK_, _WHITE_)
    self.money.message = pygame.transform.scale(self.money.message, [self.width/12, self.height/15])

    self.win_S = button.Button([s_width/4, s_height/2], "You Won!", _BLACK_, (255,215,0))
    self.win_S.message = pygame.transform.scale(self.win_S.message, [self.width/2,self.height/5])

    self.lose_S = button.Button([s_width/4, s_height/2], "You Lost :(", _BLACK_, (255,33,50))
    self.lose_S.message = pygame.transform.scale(self.lose_S.message, [self.width/2,self.height/5])

    self.JBJ_S = button.Button([s_width/5, s_height/2], "JACK-BLACK-JACK", _BLACK_, (255,215,0))
    self.JBJ_S.message = pygame.transform.scale(self.JBJ_S.message, [self.width/2,self.height/5])
    
    self.push_S = button.Button([s_width/5, s_height/2], "You Pushed.", _BLACK_, _PURPLE_)
    self.push_S.message = pygame.transform.scale(self.push_S.message, [self.width/2,self.height/5])