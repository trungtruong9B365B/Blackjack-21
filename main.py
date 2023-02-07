#Blackjack Game 21. You try to draw card as many as possible without going above 21. The program have menu and option to view past plays.

import Play
from replit import clear

game_state = True

#Loop to play the game until the player choose Quit

while game_state:
  print('Welcome to Blackjack 21!')
  action_continue = False
  while action_continue == False:
    action = input('Please select your option - (P)lay game, (R)esult, (Q)uit: ')
    #Menu option
    if action not in ['P','R','Q']:
      print('Option is invalid, please choose again!')
      action_continue = False
    #Play option
    if action == 'P':
      action_continue = True
      clear()
      result=Play.Play()
    #Record option
    if action == 'R':
      file = open("log.txt","r")
      for line in file:
        print(line)
      print('\n\n')
      action_continue = True
    #Record option
    if action == 'Q':
      exit()