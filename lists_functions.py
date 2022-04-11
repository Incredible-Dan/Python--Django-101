list1 = [1, 2, 3, 4, 5]
list2 = ['Oranges', 'Pawpaw', 'Cashew', 'Cashew', 'Banana']

list2.insert(2, 'Cherry')  # insert an item at a particular index(2)
list2.append(['Apples', 'Carrots'])
list2.remove('Pawpaw')
print(list2)
list2.append('Pawpaw')

print(list2.index('Cashew'))
print(list2.count('Cashew'))
print(list2.__contains__('Cashew'))
list2.reverse()
print(list2)

# To delete the entire list
# list2.clear()

# Joining two lists together with extend function
list1.extend(list2)

print(list1)

print(list2)
print(len(list2))

#  To duplicate a list
list3 = list2.copy()
print('This is List 3:', list3)
print(len(list3))

# To remove the last value of a list
list3.pop()
list3.pop(2)
del list3 # Deletes the entire list3
print(len(list1))
