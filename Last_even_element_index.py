n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n-1,-1,-1):
    if lst[i]%2==0:
        break
print(i)