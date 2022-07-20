# Saving user password
a = str(input('Enter Your Password ?\n'))
a1 = str(input('Confirm Your Password ?\n'))

# Creating An Attemptions
attempt = 0

# confirming user password
if a != a1:
    print('Your Entered Something Wrong\n')
    quit()
else:
    print('Your Device Is Locked\n')
    
while True: # Device has been locked 
# taking input as a password
    b = str(input('Enter Password To Unlock Your Device ?\n'))
    attempt += 1
    # checking device is locked or unlocked
    if b == a:
        print('Your Device Has Been Unlocked\n')
        
        b1 = str(input('Do You Want To Lock Your Device Again (yes- y, no- n)?\n'))
        if b1 == 'y':
            continue
        else:
            break
            
    else:
        print('You Entered Wrong Password\n')

        # exiting user input        
        if attempt == 5:
            print('You Are Out Of Your Time')
            break
        else:
            continue   