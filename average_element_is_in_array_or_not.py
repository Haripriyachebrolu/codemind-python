N=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    s+=i
    a=s//N
exist_count = lst.count(a)


if exist_count > 0:
	print('True')
else:
	print('False')