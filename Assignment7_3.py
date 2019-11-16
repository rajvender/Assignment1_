class Arithmetic:
    def __init__(self,value):
        self.value=value

    def Acceptnumber(self):
        num=int(input("enter a number"))
        self.value=num

    def ChkPrime(self):
          for i in range(2,self.value):
              if (self.value%i == 0):
                 return False
              else:
                  return True



    def ChkPerfect(self):
        '''total=0
        for i in range (1,self.value):
            if (self.value%i == 0):
               total=total+i
               if (total==self.value):
                  print(total)
                  print(self.value)
                  return True
            else:return False'''


    def SumFactors(self):
        total=0
        for i in range(1,self.value):
            if (self.value % i == 0):
                total=total+i
        print(total)
        return total

    def Factors(self):
        print("factors of ", self.value, "are")
        for i in range(1,self.value):
            if (self.value % i == 0):
             print(i)


def main():
    ob1=Arithmetic(0)
    ob1.Acceptnumber()
     #vale=ob1.ChkPerfect()
    #tot=ob1.SumFactors()
    #print(tot)
    ob1.Factors()

if __name__=="__main__":
    main()