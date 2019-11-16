class Circle:
    PI = 3.14
    def __init__(self,radius,area,circumference):
        self.radius=0
        self.area=0
        self.circumference=0
    def Accept(self):
        rad=int(input("enter the radius"))
        self.radius=rad
    def calculateArea(self):
        area= self.PI*self.radius
        self.area=int(area)
    def calculatecircumference(self):
        circumference=2*self.PI*self.radius
        self.circumference=int(circumference)

    def Display(self):
         print("radius is ",self.radius,"area is",self.area,"circumference is ",self.circumference)

def main():
 obj1=Circle(0,0,0)
 obj1.Accept()
 obj1.calculateArea()
 obj1.calculatecircumference()
 obj1.Display()
 obj2=Circle(0,0,0)
 obj2.Accept()
 obj2.calculateArea()
 obj2.calculatecircumference()
 obj2.Display()


if __name__=='__main__':
   main()