def posnum(a):
    if (a < 0):
        print("number is negative")
    elif (a > 0):
        print("number is positive")
    else:
        print("numner is zero")


print("enter a number")
a=int(input())
posnum(a)