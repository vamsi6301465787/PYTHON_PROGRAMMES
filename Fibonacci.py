n=int(input("enter any number :"))
n1,n2=0,1
n3,c=0,0
if(n<=0):
  print("enter a positive number ")
print("fibonacci series are : ")
print(n1)
print(n2)
while(c<n):
  n3=n1+n2
  n1=n2
  n2=n3
  print(n3)
  c=c+1
