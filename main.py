guesses = 1
number = 4
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number:
  print("Incorrect")
  guesses = guesses + 1
  print("Guess a number between 1 and 10")
  guess = int(input())
  if guesses == 3:
    print ("Game Over. You Used Your 3 Guesses.")
    break
else:
  print("Correct")
  print("These Are Your Ammount Of Guesses: ")
  print (guesses)
