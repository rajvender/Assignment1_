class BookStore:
    numofbooks=0
    def __init__(self,name,Author):
        self.name=name
        self.Author=Author
        BookStore.numofbooks=BookStore.numofbooks+1

    def Display(self):
     print("name of book is-",self.name,"author is-",self.Author,"number of books-",self.numofbooks)


def main():
  obj1=BookStore("Fault in our Stars","John Green")
  obj1.Display()

  obj2=BookStore("Shiva Triology","CB")
  obj2.Display()
if __name__=="__main__":
    main()

    

