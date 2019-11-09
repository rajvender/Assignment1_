
def main():
    lis=[]
    nums=int(input("enter the number of elements"))
    for i in range(nums):
         numinlist=int(input())
         lis.append(numinlist)
         min=lis[0]
    for a in (lis):
        if (a<min):
            min=a
    return min


if __name__=='__main__':
    minnum=main()
    print(minnum)