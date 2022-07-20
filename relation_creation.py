fam = {
             'mannu' : 'Brother',
             'suraj' : 'Brother',
             'sanju' : 'Brother',
             'manni' : 'Brother',
             'sagar' : 'Brother',
             'sahil' : 'Brother',
             'hunny' : 'Brother',
             'rahul' : 'Brother',
             'amar' : 'Brother',
             'kanchan' : 'Sister',
             'ritu' : 'Sister',
             'kuki' : 'Sister',
             'muskan' : 'Sister',
             'lucky' : 'Brother',
             'aman' : 'Brother',
             'babbu' : 'Brother',
             'gullu' : 'Brother',
             'silky' : 'Sister',
             'ishu' : 'Sister',
             'jassi' : 'Sister',
             }             
             
fam1 = {
             '9718813349' : 'mannu',
             '8958532870' : 'suraj',
             '9873047803' : 'sanju',
             '9971589298' : 'manni',
             '9654587350' : 'sagar',
             '8826819747': 'sahil',
             '8375088405' : 'hunny',
             'rahul' : 'Brother',
             'amar' : 'Brother',
             '9310718869' : 'kanchan',
             '9582689399' : 'ritu',
             '9636054111' : 'kuki',
             '7042547812' : 'muskan',
             '8368457859' : 'lucky',
             '9354066512' : 'aman',
             '8448367529' : 'babbu',
             '9311683208' : 'gullu',
             '9599532507' : 'silky',
             '9599532507' : 'ishu',
             '9560118913' : 'jassi',
             }

while True:
    print('Hii!!!')
    a = str(input('\nDo You Want To Check Your Relation Between You & Minty ? (y-yes, n-no)\n\n'))
    if a == 'y':
        b = str(input('Please Enter Your Name ?\n\n'))
        if b in fam:
            c = str(input('Please Enter Your Mobile Number To Confirm it\'s You ?\n'))
            if c in fam1:
                print('You Are The ',fam.get(fam1.get(c)), ' Of MINTY\n')
                

            else:
                print('You Are Stranger')
                break
        else:
             print('You are not in my database')
             break
    else:
        break    