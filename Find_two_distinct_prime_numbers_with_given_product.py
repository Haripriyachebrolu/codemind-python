n=int(input())
c=0
s=[]
for i in range(2,(n//2)+1):
    if n%i==0:
        c+=1
        s.append(i)
        if c==2:
            break
if c>1:
    print(*s)
else:
    print(-1)