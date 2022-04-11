# Normal list
countries = ['Biafra', 'United Kingdom', 'Ghana', 6, True, 'Benin Republic', 'France', 'China', 'Austria']
print(countries)

print(type(countries[2]))
print(type(countries[3]))
print(type(countries[4]))

# Using a list Constructor
countries2 = list(('Portugal', 'Singapore', 'Brazil', 7, False, 'Finland', 'Chile', 'Russia'))
print(countries2)

print(type(countries[2]))
print(type(countries[3]))
print(type(countries[4]))


# print a particular (index 1)
print(countries[1])

# print from an index to the end (1 to the end)
print(countries[1:])

# print frm a range of indexes
print(countries[2:5])

countries[0] = 'Niger'
countries[1] = 'Indonesia'
countries[2] = 'Malaysia'
print(countries)

# To get the bottom or end of a list by negative index(-)
print(countries[-1])  # this prints the last country on the list which is Austria

# To print the length of the list Items
print(len(countries)) # 7

name = 'Daniel'
num = 12

print(type(countries))
print(type(name))
print(type(num))



