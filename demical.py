a=int(input("enter number tranfer"))
base=int(input("enter base want to coverted"))
def demical(a,base):
    if a==0:
        return ""
    print(a%base)
    return demical(a//base,base)

print(demical(a,base))

