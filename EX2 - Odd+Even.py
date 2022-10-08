# Simple math, and number the user inserts that is divisible by 2 is even, otherwise odd!

user_input = input("Insert a number: ")
if int(user_input) % 2 == 0:
    print("even")
else:
    print("odd")