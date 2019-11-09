def main():
    lis=[]
    numinlist=int(input("enter the number of elements"))
    for i in range(numinlist):
        print("enter the",i,"num")
        num=int(input())
        lis.append(num)
    print(lis)
    numtofind=int(input("enter the num to find freq"))
    print(numtofind)
    totalocc = 0
    print(type(totalocc))
    for a in lis:
        if  a == numtofind:
            totalocc=totalocc+1
    return totalocc


if __name__=='__main__':
  tot=main()
  print(tot)
