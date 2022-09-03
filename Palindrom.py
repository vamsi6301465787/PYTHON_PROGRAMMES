n=int(input("Enter any number : "))
temp=n
rev=0
while(n!=0):
 rem=n%10
 rev=int(rev*10+rem)
 n=int(n/10)
if(rev==temp):
    print("Palindrome")
else :
    print("Not an Plaindrome")