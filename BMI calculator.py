w = float(input('Enter Your Weight ?\n'))
h = float(input('Enter Your Height ?\n'))
BMI = w/h**2

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obesity")