import random
print("Welcome to Craps! ")
def rematch():
  again = input("Do you want to play again? (y/n) ")
  if again.lower() == "y" or again.lower() == "yes" or again.lower() == "yeah":
    play_craps()
  else:
   print("okay, no more ")
   exit()
def roll_dice():
  return random.randint(1, 6)

def roll(point):
  input("Press anything to roll the dice again ")
  dice1 = roll_dice()
  dice2 = roll_dice()
  new_sum = dice1 + dice2
  print(f"You rolled a {dice1} and a {dice2}. your total is {new_sum} ")
  if new_sum == point:
    print("You matched your point! You win! ")
  elif new_sum == 7:
    print("You rolled a 7. Casino wins, you lose. ")
  else:
    roll(point)

def play_craps():
  input("press anything to start \n")
  dice1 = roll_dice()
  dice2 = roll_dice()
  total = dice1 + dice2
  print(f"You rolled a {dice1} and a {dice2} for a total of {total} ")
  if total in (7, 11):
   print("You won! ")
   rematch()
  elif total in (2, 3, 12):
    print("Craps! Casino wins, you lose ")
    rematch()
  else:
    point = total
    print(f"Your point is now {point} ")

    while True:
      roll(point)
      rematch()
      
play_craps()
