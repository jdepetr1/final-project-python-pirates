class Player:
  def __init__(self):
    self.cards = []

  def addCard2Hand(self, deck = None):
    card = deck.deck.pop(0)
    self.cards.append(card)
    if len(self.cards) >= 3:
      self.printHand()
  
  def printHand(self):
    print("============Player's Hand============")
    for card in self.cards:
      if card != None:
        card.printCard()
    print('')
        
  def clearHand(self):
    if self.cards:
      for _ in range(len(self.cards)):
        self.cards.pop(0)
      
  def handTotal(self):
    tot = [0,0]

    for i in range(len(self.cards)):
      if self.cards[i] != None:
        tot[0] += self.cards[i].value[0]
        tot[1] += self.cards[i].value[1]
    
    return(tot)
