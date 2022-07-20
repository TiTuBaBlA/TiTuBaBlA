# creating variables to take input

a = int(input())
b = int(input())
c = (a + b) * (b / a)

print(c)
# creating if-else condition

if a > b and c > a:
    print('c')
elif c > a and b > c:
    print('b') 
elif b > c and a > c:
    print('a')
else:
    print('You entered something special')

# creating a loop
#while True:
#    if a > b and c > a:
#        print('c')
#        print(c)