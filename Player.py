# Class definition for Player
class Player:

  # Initialization method for the Player class
  def __init__(self):
    # Initialize an empty hand for the player
    self.hand = []

  # Method to draw a card
  def draw(self, card):
    # Store the card that is received
    card_received = card
    # Add the card to the player's hand
    self.hand.append(card_received)

  # Method to discard the hand
  def discard(self):
    # Reset the hand to an empty list
    self.hand=[]

  # Method to get the current hand as a list of strings
  def get_value(self):
    # Create a list to store the current hand
    current_hand=[]
    # Iterate through each card in the hand and add the string representation of each card to the current_hand list
    for card in self.hand:
      current_hand.append(str(card))
    # Return the current hand
    return current_hand

  # Method to display the full hand
  def display_hand(self):
    # Iterate through each card in the hand and print it
    for card in self.hand:
      print(card)

  # Method to display part of the hand
  def display_some_of_hand(self, number):
    # Initialize a count variable to keep track of which cards to show
    count = 0
    # Iterate through each card in the hand
    for card in self.hand:
      # If the count equals the number, print an unknown card
      if count == number:
        print('Unknown Card')
      # Otherwise, print the card and increment the count
      else:
        print(card)
        count += 1

  # Method to calculate the value of the hand
  def hand_value(self):
    # Initialize the hand value to 0
    hand_value = 0
    # Initialize a count of aces in the hand to 0
    aces_qut = 0
    # Iterate through each card in the hand and add the value of each card to the hand value
    for card in self.hand:
      hand_value += int(card.get_value())
    # Iterate through each card in the hand
    for card in self.hand:
      # If the card is an ace, increment the aces count
      if card.rank == 'A':
        aces_qut += 1
    # If there is one ace and the hand value is less than or equal to 11, add 10 to the hand value to make the ace equal to 11
    if aces_qut == 1 and hand_value <= 11:
      hand_value += 10
    # If there are two aces and the hand has only two cards, set the hand value to 21 for a blackjack
    if aces_qut == 2 and len(self.hand) == 2:
      hand_value = 21
    # Return the hand value
    return hand_value