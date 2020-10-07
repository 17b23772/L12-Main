guesses = 1
from random import randint
number = randint(1,10)
print("Guess a number between 1 and 10")
print("You Have 3 Guesses!")
guess = int(input())
while guess != number:
  print("Incorrect")
  guesses = guesses + 1
  print("Guess a number between 1 and 10")
  guess = int(input())
  if guess == number:
    print ("Correct")
  if guesses == 3:
    print ("Game Over. You Used Your 3 Guesses.")
    break
else:
  print("Correct!")
  print("These Are Your Ammount Of Guesses: ")
  print (guesses)
