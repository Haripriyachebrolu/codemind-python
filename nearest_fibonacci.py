n=int(input())
n1=0
n2=1
sum=n1+n2
while sum<=n:
    n1=n2
    n2=sum
    sum=n1+n2

if n-n2<sum-n:
    print(n2)
elif n-n2==sum-n:
    print(n2,sum,end=' ')
else:
    print(sum)