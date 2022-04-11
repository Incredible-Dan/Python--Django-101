number_input = int(input('Enter the number to check: '))
if number_input %2 == 0:
    print('This is an even number!')
else:
    print(number_input, 'is an odd number!')
    print(number_input, 'has a remainder of', number_input % 2, 'when divided by 2' )

