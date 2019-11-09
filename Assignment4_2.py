def main():
    a1=int(input("enter the num 1"))
    a2=int(input("enter the num 2"))
    mult=lambda a1,a2:a1*a2
    fp=mult(a1,a2)
    print(fp)

if __name__=='__main__':
    main()