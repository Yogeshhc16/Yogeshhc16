n=int(input("enter the number:"))
temp=n
s=0
num=len(str(n))
while n!=0:
    r=n%10
    s+=r**num
    n=n//10
if s==temp:
    print("the number armstrong")
else:
    print("the number not armstrong")
