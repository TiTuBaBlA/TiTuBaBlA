#print('I')
#print('LOVE')
#print('python')
#a = 6
#print(a)
#print(type(a))
#b = input('Enter Here:- ')

#print(type(b))

#pokemon = ['Pikachu', 'Electric', 'Balbasaur', 'Grass', 'charmander', 'Fire', 'Squirtle', 'Water']

#poke = dict[(pokemon)]
#print(poke)

pokedex = {
                    'Totodile' : 'Water',
                    'Bayleaf' : 'Grass',
                    'Cyndequil' : 'Fire',
                    'Pikachu' : 'Electric'
                    }

#print(pokedex['Totodile'])

#a = input()
#print(pokedex.get(a))

pokedex.update({'Chimchao' : 'Electric'})
#print(pokedex.get(a))

#print(pokedex)
print('which pokemon\'s type do you want to check ?')
for i in pokedex:
    print(i)
    
a = input('\nHere :- ')
print('Type = ',pokedex.get(a))

