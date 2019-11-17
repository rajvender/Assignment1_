import os
import threading

def digit(str):
    print(os.getpid())
    aadigit=[]
    for i in str:
        if i.isdigit():
           aadigit.append(i)
    print(aadigit)

def lowercase(str):
    print(os.getpid())
    smallcharr=[]
    for i in str:
        if i.islower():
            smallcharr.append(i)
    print(smallcharr)


def uppercase(str):
    print(os.getpid())
    upper=[]
    for i in str:
        if i.isupper():
            upper.append(i)
    print(upper)


def main():
    print(os.getpid())
    stringinp=[]
    stringinp=input("enter the string")
    print(stringinp)
    #digit(stringinp)
    #lowercase(stringinp)

    small=threading.Thread(target=lowercase,args=(stringinp,))
    upper=threading.Thread(target=uppercase,args=(stringinp,))
    ddigit=threading.Thread(target=digit,args=(stringinp,))

    small.start()
    upper.start()
    ddigit.start()



if __name__=="__main__":
    main()

