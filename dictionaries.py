# Dictionaries is a key and value pair data representation.
my_dict = {
    'first_name': 'Daniel',
    'last_name': 'Idoko',
    'age': 33,
    'is_tall': True,
    'phone': '07032678290',
    'nationality': 'Biafran',
# A key can have a list as it's value pair as follows:
    'friends': ['Philip', 'Tunde', 'Ebere']

}
print(type(my_dict))
print(my_dict['first_name'])
print(my_dict['last_name'])
print(my_dict['age'])
print(my_dict['phone'])
print(my_dict['nationality'])
print(len(my_dict))
print(my_dict['friends'])

# Assigning variables to key in dictionaries.
n = my_dict['first_name']
l = my_dict['last_name']
i = my_dict['is_tall']
p = my_dict['phone']
a = my_dict['age']
nt = my_dict['nationality']
f = my_dict['friends']

# Printing the variables.

print('')

print(n)
print(l)
print(i)
print(p)
print(a)
print(nt)
print(f)
