import player

class Dealer(player.Player):
  def __init__(self, name = ""):
    self.name = name
    self.money = 9999999999
    self.cards = []

  def __str__(self):
    return f"Dealer: {self.name} using {self.deck.printDeck()}"

  def printHiddenDealerHand(self):
    print("============Dealer's Hand============\n*********")
    for i in range(2,len(self.cards)):
      print(str(self.cards[i]))

  def printDealerHand(self):
    print("============Dealer's Hand============")
    for card in self.cards:
      if card != None:
        print(str(card))
      
  def dAddCard2Hand(self, deck = None):
    card = deck.deck.pop(0)
    self.cards.append(card)

  def handTotal(self):
    tot = [0,0]

    for i in range(len(self.cards)):
      if self.cards[i] != None:
        tot[0] += self.cards[i].value[0]
        tot[1] += self.cards[i].value[1]
    
    return(tot)