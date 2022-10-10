x,y=map(int,input().split())
if x>y:
    g=x
else:
    g=y
while(True):
    if (g%x==0)and(g%y==0):
        lcm=g
        break
    g=g+1
print(lcm)