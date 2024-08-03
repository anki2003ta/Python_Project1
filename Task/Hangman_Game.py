secretWord = "CBTNuggets"
lettersGuessed = ""
failureCount = 6 #the no of turns before the player losses
while failureCount > 0 : #loop until the player made too many failed attempts
  guess = input("Enter a Letter: ")
  if guess in secretWord:
    print(f"Correct! There is one or more {guess} in the secrect word.")
  else:
    print(f"Incorrect! There are no {guess} in the secrect word. {failureCount} turn(s) left. Better Luck Next Time!!")
  lettersGuessed = lettersGuessed + guess #maintaining a list of all letters guessed
  wrongLetterCount = 0
  for letter in secretWord:
    if letter in lettersGuessed:
      print(f"{letter}", end="")
    else:
      print("_", end="")
      wrongLetterCount += 1
  print("\n")
  if wrongLetterCount == 0:
    print(f"Congratulations!! You Won. The secrect word was: {secretWord}.")
    break
else:
  print("Sorry, you lose.Try Again!!")