try:
    number = int(input('Enter a number: '))
    print(number)
except:
    print('Input must be a number! ')
finally:
    print('Operation ends here: ')