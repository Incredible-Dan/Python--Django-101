from inheritance import Products

class User(Products):
    pass
user1 = User()
print(user1.type)
print(user1.name)
print(user1.size)
print(user1.cost)