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

programContinuation = 'Y'

while programContinuation == 'Y' or programContinuation == 'y':
    userChoice = input ("Choose 'rock' or 'paper' or 'scissors': ")
    print()

    while userChoice != 'rock' and userChoice != 'paper' and userChoice != 'scissors':
        print ('Input error !!!')
        print ('Please try again')
        userChoice = input ("Choose 'rock' or 'paper' or 'scissors': ")
        print()

    else:
        while userChoice == randomChoice:
            print ('Computer also selected', userChoice)
            print ('Please try again')
            userChoice = input ("Choose 'rock' or 'paper' or 'scissors': ")
            print()  
        else:
            if userChoice == 'paper' and randomChoice == 'rock':
                print ('Computer selects', randomChoice)
                print ('Paper wraps rock')
                print ('You win !!!')
                programContinuation = input ('Type "Y" to continue or "N" to quit the game: ')
                print()
            elif userChoice == 'paper' and randomChoice == 'scissors':
                print ('Computer selects', randomChoice)
                print ('Scissors cuts paper')
                print ('Computer wins !!!')
                programContinuation = input ('Type "Y" to continue or "N" to quit the game: ')
                print()
            elif userChoice == 'rock' and randomChoice == 'paper':
                print ('Computer selects', randomChoice)
                print ('Paper wraps rock')
                print ('Computer wins !!!')
                programContinuation = input ('Type "Y" to continue or "N" to quit the game: ')
                print()
            elif userChoice == 'rock' and randomChoice == 'scissors':
                print ('Computer selects', randomChoice)
                print ('Rock smashes scissors')
                print ('You win !!!')
                programContinuation = input ('Type "Y" to continue or "N" to quit the game: ')
                print()
            elif userChoice == 'scissors' and randomChoice == 'paper':
                print ('Computer selects', randomChoice)
                print ('Scissors cuts paper')
                print ('You win !!!')
                programContinuation = input ('Type "Y" to continue or "N" to quit the game: ')
                print()
            elif userChoice == 'scissors' and randomChoice == 'rock':
                print ('Computer selects', randomChoice)
                print ('Rock smashes scissors')
                print ('Computer wins !!!')
                programContinuation = input ('Type "Y" to continue or "N" to quit the game: ')
                print()
else:
    print ('************************************************************')
    print ('********************** End of the Game *********************')
    print ('************************************************************')
