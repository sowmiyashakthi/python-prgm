n=int(input("Enter the number"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("Is a palindrome")
else:
    print("Is not a palindrome")
