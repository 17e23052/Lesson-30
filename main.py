from random import shuffle
suits = ["♥", "♦", "♣", "♠"]
deck = []
for suit in suits:
  for x in range(1,14):
    if x == 1:
      value = "A"
    elif x == 11:
      value = "J"
    elif x == 12:
      value = "Q"
    elif x == 13:
      value = "K"
    else:
      value = str(x)
    deck.append(value + suit)
shuffle(deck)
print(deck)