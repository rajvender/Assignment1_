def main():
  lis=[]
  num=int(input(("enter the number to be in the list")))
  for i in range (num):
      print("enter the ",i,"number")
      enterednum=input()
      lis.append(enterednum)
      max=lis[0]
  for a in lis:
     if(a>max):
      max=a
  return max


if __name__=='__main__':
   maxvalue= main()
print(maxvalue)