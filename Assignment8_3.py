import threading

def additionofevenlist(lis):
    evenli=0
    for i in lis:
        if (i%2)==0:
            evenli=evenli+i
    print(evenli)

def additionofoddlist(lis):
    oddli=0
    for i in lis:
        if (i%2)!=0:
            oddli=oddli+i
    print(oddli)


def main():
    li=[]
    numinlist = int(input("enter th number of elements in list"))
    for i in range(1,numinlist):
        a=int(input("enter the num",))
        li.append(a)
    print(li)

    eventhread=threading.Thread(target=additionofevenlist,args=(li,))
    oddthread=threading.Thread(target=additionofoddlist,args=(li,))

    eventhread.start()
    oddthread.start()
if __name__ == '__main__':
  main()

