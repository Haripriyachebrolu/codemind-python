n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(len(lst)):
    if lst[i]%2!=0:
        c+=1
if c>0:
    print(i)
    