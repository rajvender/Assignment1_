import threading


def odd():
   for i in range(10):
       if(i%2==0):
         print("even:",i)

def even():
    for i in range(10):
        if (i % 2 != 0):
            print("odd:", i)



def main():
    thread1=threading.Thread(target=odd)
    thread2=threading.Thread(target=even)

    thread1.start()
    thread2.start()

if __name__=="__main__":
    main()
