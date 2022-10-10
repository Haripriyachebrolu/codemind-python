n1=int(input())
n2=n1
equal=False
t=10
sq=n1**2
while n2>0:
    r=sq%t
    if r==n1:
        equal=True
        break
    n2=n2//10
    t=t*10
if (equal):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')