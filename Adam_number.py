n=int(input())
n1=str(n)[::-1]
s1=n**2
s2=int(n1)**2
sq=str(s1)
sq1=str(s2)
if (sq==sq1[::-1]):
    print('True')
else:
    print('False')