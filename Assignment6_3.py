class Arithmetic:

    def __init__(self,value1,value2):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1=int(input("enter value1 "))
        self.value2=int(input("enter value2 "))

    def Addition(self):
        print("Addition is ",self.value1+self.value2)
    def Subtraction(self):
        print("Subtraction is ",self.value1 - self.value2)
    def Multiplication(self):
        print("Multiplcation is ", self.value1 * self.value2)
    def Division(self):
        print("Division is ", self.value1 / self.value2)


def main():
    obj1=Arithmetic(0,0)
    obj1.Accept()
    obj1.Addition()
    obj1.Subtraction()
    obj1.Multiplication()
    obj1.Division()

if __name__=="__main__":
    main()