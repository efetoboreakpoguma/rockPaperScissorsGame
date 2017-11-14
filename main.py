# This program allows the User to play Rock, Paper, Scissors against the 
# computer

import random

print ('************************************************************')
print ('**************** Rock, Paper, Scissors Game ****************')
print ('************************************************************')
print ()
print ("You can only select 3 options: 'rock', 'paper' or 'scissors'")
print()

randomNumber = random.randrange (1,4)

if randomNumber == 1:
    randomChoice = 'rock'
elif randomNumber == 2:
    randomChoice = 'paper'
else:
    randomChoice = 'scissors'

userChoice = input ("Choose 'rock' or 'paper' or 'scissors': ")    

while userChoice != 'rock' and userChoice != 'paper' and userChoice != 'scissors':
    print ('Input error !!!')
    print ('Please try again')
    userChoice = input ("Choose 'rock' or 'paper' or 'scissors': ")   

else:
  while userChoice == randomChoice:
      print ('Computer also selected', userChoice)
      print ('Please try again')
      userChoice = input ("Choose 'rock' or 'paper' or 'scissors': ")
  else:
      if userChoice == 'paper' and randomChoice == 'rock':
          print ('Paper wraps rock')
          print ('You win !!!')
      elif userChoice == 'paper' and randomChoice == 'scissors':
          print ('Scissors cuts paper')
          print ('Computer wins !!!')
      elif userChoice == 'rock' and randomChoice == 'paper':
          print ('Paper wraps rock')
          print ('Computer wins !!!')
      elif userChoice == 'rock' and randomChoice == 'scissors':
          print ('Rock smashes scissors')
          print ('You win !!!')
      elif userChoice == 'scissors' and randomChoice == 'paper':
          print ('Scissors cuts paper')
          print ('You win !!!')
      elif userChoice == 'scissors' and randomChoice == 'rock':
          print ('Rock smashes scissors')
          print ('Computer wins !!!')      
