n=int(input())
a=n+1
while True:
    if (str(a)==str(a)[::-1]):
        is_palindrome=True
        break
    else:
        a+=1

b=n-1
while True:
    if (str(b)==str(b)[::-1]):
        is_palindrome=True
        break
    else:
        b-=1
d1=a-n
d2=n-b
if d1>d2:
    print(b)
elif d1==d2:
    print(b,a,end=' ')
else:
    print(a)