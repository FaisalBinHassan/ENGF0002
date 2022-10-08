# This excersie is used to solve for the greatest common divisor

def Gcd(a,b):
    while not a==b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a

ax = 42
bx = 30
print("gcd of", ax , "and", bx , "is", Gcd(ax,bx) )