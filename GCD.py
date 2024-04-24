def gcd(a,b):
    if b == 0:
        return a ;
    return gcd(b,a%b)
try:

    a=int(input("enter number 1\t"))
    b=int(input("enter number 2\t"))
    print("Greatest common denominator of a and b ",gcd(a,b))
except ValueError as err:
    print("invalid Input:",err) 
