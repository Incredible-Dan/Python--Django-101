# Strings are just plain Text in a single or double quotes.
name = "Daniels"
print(name) # Daniel

print('Hi. \nHow are you ?') # use backslash n(\n) to print on a new line
                            # Hi.

                            # How are you ?
print('Hi. \'How are you ?')  # use \ to add single quote to a string

# Special functions in String

print(name.upper())
print(name.islower())
print(name.lower().islower())
print(name[1].capitalize())
print(len(name))
print(name.index('e'))
print(name.replace('s', 'z'))