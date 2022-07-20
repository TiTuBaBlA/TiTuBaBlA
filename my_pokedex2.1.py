opt = ['Type', 'Attack', 'Region']

pokedex = {
                    'Totodile' : 'Water',
                    'Bayleaf' : 'Grass',
                    'Cyndequil' : 'Fire',
                    'Pikachu' : 'Electric'
                    }
pokedex1 = {
                    'Totodile' : 'Hydro Pump',
                    'Bayleaf' : 'Razor Leaf',
                    'Cyndequil' : 'Flamethrower',
                    'Pikachu' : 'Electro Web'
                    }
pokedex2 = {
                    'Totodile' : 'Jhoto Region',
                    'Bayleaf' : 'Jhoto Region',
                    'Cyndequil' : 'Jhoto Region',
                    'Pikachu' : 'Kanto Region'
                    }

def dex(pokedex):
    for j in pokedex:
        print(j)

while True:    
    print('what do you want to check ?\n')
    for i in opt:
        print(i)
        
    a = str(input('\nHere:- '))

    if a == 'Type':
        print('\nWhich pokemon\'s Type Do You Want To Check ?\n')
    
        dex(pokedex)
        print('Type = ',pokedex.get(input('Here:- ')))
    
    elif a == 'Attack':
        print('\nWhich Pokemon\'s Attack Do You Wanna Check ?\n')
        
        dex(pokedex)
        print('Attack = ',pokedex1.get(input('Here:- ')))
        
    elif a == 'Region':
        print('\nWhich Pokemon\'s Region Do You Wanna Check ?\n')
        
        dex(pokedex)
        print('Region = ',pokedex2.get(input('Here:- ')))
        
    else:
        print('You\'re not poke fan')

    b = input('\nDo You Wanna Check Again ?\n')
    
    if b != 'yes':
        break
    else:
          continue  