import random 

lower_limit = int(input("Lower Limit Range:"))
upper_limit = int(input("Upper Limit Range:"))

target = random.randint(lower_limit , upper_limit)
print(target)
while True:
  userChoice = input("Guess the target or Quit(Q) :")
  if(userChoice == 'Q'):
    break
  userChoice = int(userChoice)
  if(userChoice == target):
    print("Success : Correct Guess!!")
    break
  elif(userChoice < target):
    print("Your no was too small. Take a bigger guess..")
  else:
    print("Your no was too large. Take a smaller guess..")
print("----GAME OVER----")