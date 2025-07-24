# num=2
# while num <=20:
#     is_prime =True
#     i=2
#     while i<num:
#         if num %i==0:
#             is_prime=False
#             break
#         i+=1
#     if is_prime:
#         print(num)
#     num+=1

for num in range(2,21):
   is_prime=True
   for i in range(2,num):
      if num%i==0:
       is_prime=False
    #   break
   if is_prime:
     print(num)
