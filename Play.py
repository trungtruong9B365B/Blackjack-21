import Card
import Player
import Game
from replit import clear
from datetime import datetime

#Function to log the result of game include date and time, current bank #balance, amount bet money, player final hand and dealer final hand
def logStats(dealer_hand,player_hand,result,bank,bet):
  file = open('log.txt','a')
  now = datetime.now()
  dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
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
             
#Function to set up the Deck of card, manage player's money and call out the play from game to start Black jack 21
def Play():
  player = Player.Player()
  dealer = Player.Player()
  bank = 0
  bet = 0
    
  deck = Card.Deck()
  deck.shuffle()
  
  while True:
    #SETUP MONEY
    while bank == None or bank <= 0:
      try:
        bank = int(input('Please input your starting money: $'))
      except:
        print('Please input a number!')
        bank = None
        continue
      if bank <= 0:
       print('Please input a positive amount!')
    print('Player bank: $', bank)
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
    clear()


    #START GAME
    print('Player bank: $', bank)
    print('You bet: $', bet)
    bank -= bet
    print('Card in deck: ', deck.card_left())
    result = Game.start(deck,dealer,player)
    logStats(dealer.get_value(),player.get_value(),result,bank,bet)
    if result == 'win':
      bank += 2*bet
    if result == 'tie':
      bank += bet
    if bank > 0:
      print('Your bank balance is: $',bank)
    else:
      print('You have ran out of money!')
    game_state = input('\nInput any key to continue or (Q)uit the game: ')
    if game_state == "Q":
      clear()
      return
    player.discard()
    dealer.discard()
    clear()
    
    #If not enough card left in the deck, deck will be reset
    if deck.card_left() <= 10:
      print('\nNot enough card in deck. Deck is shuffled!\n')
      deck.reset()
      deck.shuffle()