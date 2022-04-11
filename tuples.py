# Tuples are used to store multiple items in a single variable
# Tuples are immutable, you can't change the values.
some_numbers = (5, 2, 'man', True, 4, 5, 7, 6)
# Tuple constructor
numbers = tuple((1, True, 'dog', 'fish'))
print(numbers)
print(some_numbers[2]) # value at index 2 = 4
print(some_numbers)
print(type(some_numbers[2])) #class 'tuple'