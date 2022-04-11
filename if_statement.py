# This is a conditional statement that executes
# if a certain condition is True.

# I write a number
# if the number is divisible by 2
# then the number is an even number
# but if the number is not divisible by 2
# the the number is an odd number

# a = 5
# b = 5
# if a > b:
#     print(a, 'is greater than ', b)
# elif a < b:
#     print(a, 'is less than ', b)
# else:
#     print(a, 'is neither greater nor equal to ', b)

man = False
single = False
age = int(input('Enter your age:'))

if type(age) == int and age >= 18:
    print('You are an adult')
elif age <= 17:
    print('You are not yet an adult')

if man == True and single == False:
    print('The Man is Married!')


elif man == True and single == True:
    print('This must be a  single man')

elif man == False and single == True:
    print('This must be a single woman!')

elif man == False and single == False:
    print('This must be a married woman')

else:
    print('Both is either teenage boy  or a teenage girl and neither of them is married.')
