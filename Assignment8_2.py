import threading


def evenfactor(num):
    total = 0
    for i in range(num):
        if (i%2 == 0):
            total=total+i
    print(total)

def oddfactor(num):
    total = 0
    for i in range(num):
        if ((i%2)!= 0):
         total=total+i
    print(total)

def main():
    num=int(input("enter the num"))
    t1=threading.Thread(target=evenfactor,args=(num,))
    t2=threading.Thread(target=oddfactor,args=(num,))

    t1.start()
    t2.start()

if __name__=="__main__":
    main()
