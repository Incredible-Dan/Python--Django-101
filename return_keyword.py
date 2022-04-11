# Return statements are used to
# get a response from the task being executed and or
# when the current or said task executes

def return_function():
    return 6+4


print(return_function())


def add_numbers(num1, num2):
    return num1 + num2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print(add_numbers(num1, num2))