n=int(input())
s=0
p=1
while n>0:
    r1=n%10
    p*=r1
    s+=r1
    n=n//10
d=p-s
print(d)