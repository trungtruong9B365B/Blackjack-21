import Card


class Player:

  def __init__(self):
    self.hand = []

  def draw(self, card):
    card_received = card
    self.hand.append(card_received)

  def discard(self):
    self.hand=[]

  def get_value(self):
    current_hand=[]
    for card in self.hand:
      current_hand.append(str(card))
    return current_hand

  def display_hand(self):
    for card in self.hand:
      print(card)

  def display_some_of_hand(self, number):
    count = 0
    for card in self.hand:
      if count == number:
        print('Unknown Card')
      else:
        print(card)
        count += 1


#Calcuate hand rank. First part is calculating hand value assuming Ace = 1. Second pass is checking if Aces = 11 will make the player go above 21. If it is not, Ace rank will be 11. If there is two Aces, it is blackjack and player will get 21.
        
  def hand_value(self):
    hand_value = 0
    aces_qut = 0
    for card in self.hand:
      hand_value += int(card.get_value())
    for card in self.hand:
      if card.rank == 'A':
        aces_qut += 1
    if aces_qut == 1 and hand_value <= 11:
      hand_value += 10
    if aces_qut == 2 and len(self.hand) == 2:
      hand_value = 21
    return hand_value

