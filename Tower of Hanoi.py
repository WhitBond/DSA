def h(n,start,end):
    if n==1:
        print("move disk",n," from peg source",start,"to Destination ",end)
    else:
        other=6-(start + end)
        h(n-1,start,other) 
        print("move disk",n," from peg source",start,"to Destination ",end)
        h(n-1,other,end)
n=int(input("enter number of disk"))
h(n,1,3)
