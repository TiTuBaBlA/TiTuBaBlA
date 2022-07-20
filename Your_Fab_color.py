import random
colors = ['Red', 'Yellow', 'Green', 'Blue', 'Violet', 'Black', 'White', 'Orange', 'Brown']
len = 1
while True:
    c = "". join(random.sample(colors, len))
    print(c)
    inp = str(input('\nThis Is Your Favorite Color (y- yes, n-no) ?\n'))
    if inp == 'y':
        print('\ncongratulation ! You Got Your Favorite Color')
        break
    else:
        print('\nOh no !! My Bad')
        
        inp1 = str(input('\nDo You Wanna Guess Again (y-yes, n-no)?\n'))
        if inp1 != 'y':
            break
        else:
             continue