class BankAccount:
    ROI=10.5
    def __init__(self,name,Amount):
        self.name=name
        self.Amount=Amount

    def Display(self):
         print("Name is",self.name,"Amount is",self.Amount)

    def Deposit(self):
        depositedAmount = int(input("enter the amount to be deposited"))
        self.Amount = self.Amount + depositedAmount

    def WithDraw(self):
        withdrawamout=int(input("enter amount to be withdrawn"))
        self.Amount=self.Amount - withdrawamout

    def CalculateInterest(self):
        Interest=((self.Amount*BankAccount.ROI*12)/100)
        print(Interest)



def main():
 ob1=BankAccount("Raj",10000)
 ob1.Deposit()
 ob1.WithDraw()
 ob1.Display()
 ob1.CalculateInterest()

if __name__=="__main__":
    main()