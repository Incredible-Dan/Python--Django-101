numb1 = int(input('Enter the first number: '))
numb2 = int(input('Enter the second number: '))
op = input('Enter the operation symbol: ')

if op == '+':
    print('The result of this operation is :', numb1 + numb2)
elif op == '-':
    print('The result of this operation is :', numb1 - numb2)
elif op == '*':
    print('The result of this operation is :', numb1 * numb2)
elif op == '/':
    print('The result of this operation is :', numb1 / numb2)
else:
    print('Operator not valid!.')



