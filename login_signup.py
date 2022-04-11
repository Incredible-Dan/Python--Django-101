print('Create your Account')
username = input('Input username: ')
password = input('Input password: ')
if username == password:
    print('user', 'admin', 'created successfully')
else:
    print('Invalid admin data.')

print('Login now')
username2 = input('Enter your username: ')
password2 = input('Enter your password: ')
if username2 == password2:
    print('user logged in successfully')
else:
    print('Invalid user data.')
