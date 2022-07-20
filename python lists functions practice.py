# making list in python

family = ['sunderi', 'Dalip', 'Sona', 'Minty', 'Muskan']
print(family)
print(family[0])
print(family[1])
print(family[2])
print(family[3])
print(family[4])

# using lists functions

numbers = ['9', '7','5','3','1']
numbers.insert(5, 11)
print(numbers)

numbers.remove(11)
print(numbers)

numbers.append(13)
print(numbers)

# copied codes from internet
my_list = ['p', 'r', 'o', 'b', 'e']

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])