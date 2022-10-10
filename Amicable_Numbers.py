a=int(input())
b=int(input())
s=0
s1=0
for i in range(1,(a//2)+1):
    if a%i==0:
        s=s+i
for i in range(1,(b//2)+1):
    if b%i==0:
        s1=s1+i
if s==b and s1==a:
    print('Amicable')
else:
    print('Not Amicable')