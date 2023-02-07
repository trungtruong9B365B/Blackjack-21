import Card
import Player
import Game
from replit import clear
from datetime import datetime

#Function to log the result of game include date and time, current bank balance, amount bet money, player final hand and dealer final hand
def logStats(dealer_hand, player_hand, result, bank, bet):
  # Open the file in append mode to add the log entry at the end of the file
  file = open('log.txt', 'a')
  # Get the current date and time
  now = datetime.now()
  dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
  # Write the log entry to the file
  file.write('\n\nDate and Time = ' + dt_string)
  file.write('\nDealer Card: ')
  for card in dealer_hand:
    file.write(card + ', ')
  file.write('\nPlayer Card: ')
  for card in player_hand:
    file.write(card + ', ')
  file.write('\nBank Balance before Bet: $' + str(bank))
  file.write('\nBet Amount: $' + str(bet))
  file.write('\nResult: ' + result)
  # Close the file
  file.close()
             
# Function to set up the Deck of cards, manage player's money and call out the play from game to start Blackjack 21
def Play():
  # Create player and dealer objects
  player = Player.Player()
  dealer = Player.Player()
  # Initialize bank balance
  bank = 0
  bet = 0

  # Create deck object and shuffle it
  deck = Card.Deck()
  deck.shuffle()

  # Start the game loop
  while True:
    #Prompt the player for bet until a valid input is entered
    while bank == None or bank <= 0:
      try:
        bank = int(input('Please input your starting money: $'))
      except:
        print('Please input a number!')
        bank = None
        continue
      if bank <= 0:
        print('Please input a positive amount!')
    # Print the player's bank balance
    print('Player bank: $', bank)
    # Input bet amount and validate it
    bet = 0
    while bet == None or bet <= 0 or bet > bank:
      try:
        bet = int(input('Please input your bet: $') or "5")
      except ValueError:
        print('Please input a number!')
        bet = None
        continue
      if bet <= 0:
        print('Please input a positive amount!')
      if bet > bank:
        print('You do not have enough money in bank for this bet!')
    # Clear the console
    clear()

    # Print the player's bank balance and subtract the bet amount from bank
    print('Player bank: $', bank)
    print('You bet: $', bet)
    bank -= bet
    #Display remaining card in deck
    print('Card in deck: ', deck.card_left())
    result = Game.start(deck,dealer,player)
    #Log current session result
    logStats(dealer.get_value(),player.get_value(),result,bank,bet)
    #Update the bank balance based on the result of the game
    if result == 'win':
      bank += 2*bet
    if result == 'tie':
      bank += bet
    #Show the player's updated bank balance
    if bank > 0:
      print('Your bank balance is: $',bank)
    else:
      print('You have ran out of money!')
    #Prompt the player to continue or quit the game
    game_state = input('\nInput any key to continue or (Q)uit the game: ')
    if game_state == "Q":
      clear()
      return

    # Discard the player's cards
    player.discard()
    # Discard the dealer's cards
    dealer.discard()
    clear()
    
    #If not enough card left in the deck, deck will be reset
    if deck.card_left() <= 10:
      print('\nNot enough card in deck. Deck is shuffled!\n')
      deck.reset()
      deck.shuffle()