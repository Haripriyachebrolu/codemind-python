 
N=int(input())
test_list = list(map(int,input().split()))

n=int(input())


exist_count = test_list.count(n)


if exist_count > 0:
	print('True')
else:
	print('False')
        