from src import card
import random

class Deck:
  _NUM_DECKS_ = 2
  _SUITS_ = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
  _NAMES_ = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
  _NUM_SUITS_ = len(_SUITS_)
  _NUM_CARDS_PER_SUIT_ = len(_NAMES_)
  _NUM_CARDS_PER_DECK_ = _NUM_CARDS_PER_SUIT_ * _NUM_SUITS_
  _TOP_OF_DECK_ = 0
  
  def __init__(self):
    self.deck = []
    for _ in range(2):
      for value in range(1,53):
        card0 = card.Card(Deck._NAMES_[value% Deck._NUM_CARDS_PER_SUIT_], Deck._SUITS_[(value//Deck._NUM_CARDS_PER_SUIT_)-1])
        self.deck.append(card0)

  def shuffle(self):
    for i in range(Deck._NUM_DECKS_ * Deck._NUM_CARDS_PER_DECK_):
      card_rand0 = random.randint(0,51)
      card_rand1 = random.randint(0,51)
      self.deck[card_rand0], self.deck[card_rand1] = self.deck[card_rand1], self.deck[card_rand0]

  def __str__(self):
    return "Deck of "+str(len(self))+" cards. "+str(Deck._NUM_CARDS_PER_SUIT_)+" cards per each of the " + str(Deck._NUM_SUITS_)+" suits."
    
  def printDeck(self):
    for ecard in self.deck:
      ecard.printCard()