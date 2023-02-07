#Testing area

import Card
import Player

card1 = Card.Card('A','Heart')
card2 = Card.Card('A','Spades')

player = Player.Player()

player.draw(card1)
player.draw(card2)

player.display_hand()
print(player.hand_value())