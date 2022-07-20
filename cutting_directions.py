vegitables = {'vegitable' : 'cutting directions'}
fruits = {'fruits' : 'cutting directions'}

while True:
    inp = str(input('What Do Your Want To Cut Vegitables Or Fruits ?\n')).lower()
    if inp == 'vegitables':
        inp1 = str(input('Which Vegitable Do You Wanna Cut ?\n')).lower()
        print(vegitables.get(inp1))
    elif inp == 'fruits':
        inp2 = str(input('Which Fruit Do You Wanna Cut ?\n')).lower()
        print(fruits.get(inp2))

        c = str(input('Do You Wanna Cut Something Again ?\n')).lower()
        if c != 'yes':
            break
        else:
            continue
    else:
         print('Something Went Wrong !!!!')