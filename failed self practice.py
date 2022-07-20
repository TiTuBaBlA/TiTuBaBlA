states = { 'Punjab': 100, 'Delhi' : 98, 'Rajasthan': 89, 'Heydrabad': 87, 'Sikkim' : 78, 'Tamil Nadu' : 76, 'Uttar Pardesh' : 67}



while True:

    cute = str(input('Enter Your State From Given Below To Measure How\'s You Cute ?\n\nPunjab\nDelhi\nRajasthan\nHeydrabad\nSikkim\nTamil Nadu\nUttar pradesh\n\nEnter Here:-'))

    print(str(states.get(cute))+ '%')
    
    a = str(input('\nDo You Want To Check Again ?\n'))

    if a == 'no':
        print('Thanks For Playing')
        exit()

    else:
        continue
        
        