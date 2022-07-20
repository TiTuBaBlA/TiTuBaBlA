print('WELCOM TO THE GAME\n\n')

print('YOU\'RE IN THE GAME ZONE\n\n')

Choice = input('What Do You Want- CORN or WATER ?\n')


if Choice == 'corn':
           
           masala = input('How Much Masala Do You Want In Corn ?\n')
           sure = input(masala + '% Are You Sure ?\n')
           if sure == 'yes':
               print('You\'re Corn Is Ready To Eat')
               print('\n\ncreated by:- IDLaBaNa')
           else:
               print('Sorry')
               print('\n\ncreated by:- IDLaBaNa')
        
if Choice == 'water':
                    water = input('How Much Water Do You Want ? (Please Enter In Liter)?\n')
                    conf = input('Do You Want ' + water + ' Liters ?\n')
                    
                    if conf == 'yes':
                           print('Thanks For Ordering')
                           print('\n\ncreated by:- IDLaBaNa')
                    else:
                            print('Sorry We Don\'t Have It')
                            print('\n\ncreated by:- IDLaBaNa')
            