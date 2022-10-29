from statistics import mean 
N=int(input())

inp_lst = list(map(int,input().split()))

sum_lst = sum(inp_lst)

lst_avg = sum_lst/len(inp_lst)
 


print("{:.2f}".format(lst_avg))
