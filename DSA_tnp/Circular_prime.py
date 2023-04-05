def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        rotated_n = int(str_n[i:] + str_n[:i])
        if not is_prime(rotated_n):
            return False
    return True


limit = int(input("Enter the limit: "))    
ans=[]
for i in range(2, limit):
    if is_circular_prime(i):
        ans.append(i)
print(*ans,sep=',')        
    





        
    
            