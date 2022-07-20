n1 = int(input('Enter Your First Number ?\n'))
op = input('Put Your Opration !!\n+, -, *, / \n')
n2 = int(input('Enter Your Second Number ?\n'))

if n1 == 42  or n2 == 2 and op == '+':
    print('Total = 555')
elif n1 == 52 or n2 == 33 and op == '-':
    print('Total = 63')
elif n1 == 176 or n2 == 74 and op == '*':
    print('Total = 96')
elif n1 == 196 or n2 == 125 and op == '/':
    print('Total = 12')


elif op == '+':
    print('Total = ', n1 + n2)
elif op == '-':
    print('Total = ', n1 - n2)
elif op == '*':
    print('Total = ', n1 * n2)
elif op == '/':
    print('Total = ', n1 / n2)
else:
    print('Error')