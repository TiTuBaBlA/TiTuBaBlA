a = int(input('Enter Your Number?\n'))
b = int(input('Enter Your Number That Your Want To Find Percent ?\n'))

ans = (a / b) * 100

if a < 0:
    print('Ops !! You entered greater number than 25. Try again !!')
else:
    print(str(ans) + '%')
    