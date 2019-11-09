

def main():
    li= []
    num=int(input(("enter the number of items to be stored in the list")))
    for i in range(1,num+1):
        print("enter the",i ,"number")
        enterednum=input()
        li.append(enterednum)
    print(li)






if __name__=="__main__" :
    main()