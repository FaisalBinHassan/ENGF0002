# Algotithm
# Starting from 1 till 100, we pass by each number, and we check the 3 cases:
# 1- if it's modolo by 3 && 5 then ifs "FizzBuzz"
# 2- if it's modolo by 3 ONLY then ifs "Fizz"
# 3- if it's modolo by 5 ONLY then ifs "Buzz"
# Else print the number itself


for x in range(1,100):
    if (x % 3 == 0) & (x % 5 == 0):
        print("FizzBuzz")
    elif (x % 3 == 0):
        print("Fizz")
    elif (x % 5 == 0):
        print("Buzz")
    else:
        print(x)