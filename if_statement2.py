value = int(input('Enter a number: '))
if value %3 == 0:
    print(value, 'can be divided by 3 without remainder.')
else:
    print(value, ' has a remainder of ', value % 3, 'when divided by 3. ')
