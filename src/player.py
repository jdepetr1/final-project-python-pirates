class Player:
  def __init__(self, name="", money=0):
    self.name = name
    self.money = money
    self.cards = []

  def __str__(self):
    return f"Player: {self.name}\n Money: ${self.money}"

  def addCard2Hand(self, deck = None):
    card = deck.deck.pop(0)
    self.cards.append(card)
  
  def printHand(self):
    print("============Player's Hand============")
    for card in self.cards:
      if card != None:
        card.printCard()
  
  def handTotal(self):
    tot = [0,0]

    for i in range(len(self.cards)):
      if self.cards[i] != None:
        tot[0] += self.cards[i].value[0]
        tot[1] += self.cards[i].value[1]
    
    return(tot)