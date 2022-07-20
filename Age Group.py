age = int(input('Enter Your Age ?\n'))
if (age <= 11 and age >= 0):
    print("Child")
elif (age <= 17 and age >= 12):
    print("Teen")
elif (age <= 100 and age >= 18):
    print("Adult")