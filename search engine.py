# creating a search engine

text = input('Enter Your Text Here :-\n').lower()
word = input('Enter Your Word Here:-\n').lower()


# declaring a function
def search(x, y):

    if y in x:
        return("Word found")
    else:
        return ("Word not found")

# finish
print(search(text, word))