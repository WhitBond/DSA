def fibIterative( n ):
    fibVal = 0
    currVal = 1
    lastVal = 0
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        for ii in range(2, n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
            print(fibVal)
    return fibVal

def fibRecursive( n ):
    fibVal = 0
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal
try:
    n=int(input("enter your number"))      
    a=fibRecursive(n)
    print("Recursive method ",a)
    
    b=fibIterative(n)
    print("intertive method ",a)
except ValueError as err:
    print("invalid input",err)
