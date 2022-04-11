class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name = input('Enter your name: ')
age = input('Enter your age: ')
person1 = Person(name, age)
print('Your name is: ' + person1.name)
print('Your name is: ' + person1.age)