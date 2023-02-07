import Card
import Player
import Game

#Deal card from the deck and the the player take the card
def deal(deck,player):
  card_deal = deck.deal()
  player.draw(card_deal)
  return card_deal

#Add decoration around player card
def display_player_card(player):
  print('================')
  print('Player card:')
  print('------------')
  player.display_hand()
  print('------------')
  print('Your rank is:',player.hand_value())
  print('================:')

#Add decoration around dealer card
def display_dealer_card(dealer):
  print('================')
  print('Dealer card:')
  print('------------')
  dealer.display_hand()
  print('------------')
  print('Dealer rank is:',dealer.hand_value())
  print('================:')

#Add decoration around dealer card when call out the function display some of dealer card  
def display_dealer_card_partial(dealer,number):
  print('================')
  print('Dealer card:')
  print('------------')
  dealer.display_some_of_hand(number)
  print('================')

#Function to run the Black Jack 21 game
def start(deck,dealer,player):

#Deal 2 card to dealer and player
  deal(deck,dealer)
  deal(deck,player)
  deal(deck,dealer)
  deal(deck,player)
  display_dealer_card_partial(dealer,1)
  display_player_card(player) 

#If player card is already 21, move on to check dealer card
  if player.hand_value()==21:
    action_continue = True
  else:
    action_continue = False
  #Loop player action until player get 21 or player choose Stand. The game will go to Player lose if player get above 21
  while action_continue == False:
    action=input('\nPlease choose your option (H)it, (S)tand: ')
    if action not in ['H','S']:
      print('Action not valid, please choose again!')
      action_continue = False
    elif action == "H":
      action_continue = False
      card = deal(deck,player)
      print('\nYou drew a card. It is',card)
      print('Your current rank:',player.hand_value())
      if player.hand_value()==21:
        action_continue = True
      #The game will stop if player get above 21
      if player.hand_value()>21:
        print('\nYou have gone bust!')
        return 'lose'
    else:
      action_continue = True
  print('\nDealer reveal their other card. It is',dealer.hand[1])
  
  #Dealer draw card until Rank is above 17
  while dealer.hand_value() <= 17:
    card = deal(deck,dealer)
    print('Dealer drew a card. It is',card)
  display_dealer_card(dealer)
  display_player_card(player)

  #Check rank for dealer and player and output the result
  if dealer.hand_value() > 21:
    print('\nDealer went bust. You win!')
    return 'win'
  if player.hand_value() > dealer.hand_value():
    print('\nYou win!')
    return 'win'
  if player.hand_value() == dealer.hand_value():
    print('\nIt is a tie!')
    return 'tie'
  if player.hand_value() < dealer.hand_value():
    print('\nYou lose!')
    return 'lose'
  