from src import player

class Dealer(player.Player):
  def __init__(self):
    super()
    self.cards = []

  def __str__(self):
    return f"Dealer: {self.name} using {self.deck.printDeck()}"

  def addCard2Hand(self, deck = None):
    card = deck.deck.pop(0)
    self.cards.append(card)
    if len(self.cards) >= 4:
      self.printHand()

  def printHand(self):
    print("============Dealer's Hand============")
    if len(self.cards) == 3:
      print(f"***************\n***************\n{str(self.cards[2])}")
      print('')
    else:
      for card in self.cards:
        if card != None:
          print(str(card))
      print('')