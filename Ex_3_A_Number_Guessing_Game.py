# Exercise 3 From Code With Harry Channel
# Making A Guessing Game 
print('A Number Guessing Game\n\n')
print('WELCOME TO IDLaBaNa\'s GAME🙈🙉🙊\n\n')

game = str(input('Do You Want To Play This Game ?\n'))
if game == 'yes':
        print('\nYou Entered In The Game Zone\n\n👇🏻🎮👇🏻🎮👇🏻🎮\n')
else:
        exit()
        # Giving A Number And a Number of attemptions
import random

n = random.randint(1,100)

attempt = 1 # Making A while loop

while True: # Taking Input From User
    inp = int(input('GUESS A NUMBER between 0 to 100 ?\n'))

# Checking Given Number Input By User
    if inp > n:
        print('\nIts Smaller Than ' + str(inp) + '\n')
        attempt += 1
    elif inp < n:
        print('\nIts Greater Than ' + str(inp) + '\n')
        attempt += 1
    elif inp == n:
        print('\n\nCongratulations You Win The Game In ' + str(attempt) + ' Attempt')
        print('\n\n\nCreated By IDLaBaNa  : )  °_°')
        break
    else:
        continue

# Ending The Game
    if attempt == 10:
        print('Ops !! You lose Try Your Best Again Next Time  : (  :(  ')
        print('\n\n\nCreated By IDLaBaNa  : )  °_°')
        break
    else:
         continue    