n=int(input())
temp=n
x=0
while n!=0:
    n1=n%10
    x+=n1**3
    n=n//10
if x==temp:
    print("armstrong")
else:
    print("not")
