import math
n=int(input("enter any number : "))
d=int(math.log10(n))+1
sum=0
temp=n
while(n!=0):
  rem=n%10
  sum=int(sum+pow(rem,d))
  n=int(n/10)
if(sum==temp):
  print("Amstrong number")
else :
  print("Not an Amstrong")