num=int(input("enter the number:"))
fact=1
if num==0:
    print("the number is invalid")
elif num == 0 and num ==1:
    print(f"{num} !={fact}")
else:
  for i in range(2,num+1):
   fact=fact*i
  print(fact)