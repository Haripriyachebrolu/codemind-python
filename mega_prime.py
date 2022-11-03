def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True
    
n = int(input())
if prime(n) == True:
    is_mega_prime = True
    while n > 0:
        a = n % 10
        if prime(a) == False:
            is_mega_prime = False
            break
        n = n // 10
    if is_mega_prime == False:
        print('Not Mega Prime')
    else:
        print('Mega Prime')
else:
    print('Not Mega Prime')



