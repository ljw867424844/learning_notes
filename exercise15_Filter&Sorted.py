def get_prime(n): 
    nums = list(range(2, n + 1)) 
    prime = []
    
    while nums: 
        p = nums[0] 
        prime.append(p) 
        nums = list(filter(lambda x, p=p: x % p > 0, nums[1:]))
        
    return prime 

print(get_prime(100))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse=True)

print(L2)
print(L3)
