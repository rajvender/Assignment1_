def main():
    def fun():
        print("how many first even numbers you want")
        a = int(input())
        i = 2
        b = i * a + 1
        for j in range(1,b):
            if j%2==0:
                print(j)
    fun()
if __name__=='__main__':
    main()







