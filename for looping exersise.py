trac = [ ['Vim Bar', 10], [ 'Godreg', 4], [ 'Sugar', 10], [ 'Atta', 20], [ 'Fortune', 5] ]
#dict1 = dict(trac)
#print(dict1)


for item, value in trac:
    if value > 6:
        print(item, 'is' , value)
    
   # print(item)
   
   
   
   #list = [2,3,4,5,6,7]

#for x in list:
#    if (x % 2 == 1 and x > 4):
#        print(x)
#x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
#sum = 0
#for num in x:
#    sum += num
#print(sum)
items = [ int, float, 'Lovely', 'Hacker', 'python', 2, 2653, 3, 44, 36, 6, 1029, 26]


for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)
