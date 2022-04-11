def hello_function(name, age):  # function with two arguements
    print('Mr ' + name, '!', 'you are', age, 'years old')


hello_function('Daniel', 34)


# Passing in various parameters as a tuple
def hello(*names):
    print('Mr ' + names[4], '!', 'you are welcome!')


hello('Hans', 'Sam', 'Peter', 'Mary', 'Dan', 'Lovelyn')


# functions with user input
def words(name, age):
    print('Mr ' + name, '!,', 'you are', age, 'years old')


name = input('Enter your name:')
age = int(input('Enter your age:'))

words(name, age)
