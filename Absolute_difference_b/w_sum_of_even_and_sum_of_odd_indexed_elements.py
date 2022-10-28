n=int(input())
lst=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(lst)):
    if i%2==0:
        s1+=lst[i]
    else:
        s2+=lst[i]
d=abs(s1-s2)
print(d)
    
        