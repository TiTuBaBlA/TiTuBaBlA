# Making a Faulty Calculator
# Exercise 2 Form Code with Harry

# First We Make Simple Calculator
n1 = int(input('Enter Your First Number ?\n'))
op = input('Put Your Operation !\n - ,+ ,* , / !\n')
n2 = int(input('Enter Your Second Number ?\n'))


#if op == '-':
#    print('Total = ', n1 - n2)
#elif op == '+':
#    print('Total = ', n1 + n2)
#elif op == '*':
#    print('Total = ', n1 * n2)
#elif op == '/':
#    print('Total = ', n1 / n2)
#else:
#    print('Error')
    
# Now We Make It Faulty !!!!

if n1 == '42' or n2 == '2' and n1 * n2:
    print('555')
else:
    print(n1 * n2)
