country_file = open('countries.txt', 'r')
print(country_file.readable())
# print(country_file.readlines()[3])
for lines in country_file.readlines():
    print(lines)
country_file.close()
