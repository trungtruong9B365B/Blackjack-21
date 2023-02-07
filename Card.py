from random import shuffle

# Class definition for Card
class Card:

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    
#Define Rank and Suit for Card
  def get_value(self):
    if self.rank == 'A':
      return 1
    elif self.rank in ['J', 'Q', 'K']:
      return 10
    else:
      return self.rank

  def __str__(self):
    return str(self.rank) + " of " + self.suit

#Define Deck 
class Deck:
  deck = []
  
#Populate Deck with Cards Object
  def __init__(self):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    for suit in suits:
      for rank in ranks:
        card = Card(rank, suit)
        self.deck.append(card)
        
#Shuffle the deck to random order
  def shuffle(self):
    shuffle(self.deck)

#Deal the card to a player
  def deal(self):
    card_deal = self.deck.pop(1)
    return card_deal

#Display all card in the dec
  def display(self):
    for card in self.deck:
      print(card)

#Count how many card are left in the deck
  def card_left(self):
    count = 0
    for card in self.deck:
      count += 1
    return count

#Discard all card and then initialize a new deck
  def reset(self):
    self.deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    for suit in suits:
      for rank in ranks:
        card = Card(rank, suit)
        self.deck.append(card)