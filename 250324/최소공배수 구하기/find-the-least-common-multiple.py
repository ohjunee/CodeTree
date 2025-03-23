n, m = map(int, input().split())

# Please write your code here.

def get_gcd(n,m):
    for i in range(1, min(m,n)+1, 1):
        if n%i==0 and m%i==0:
            res = i
    return res

def get_sol(n,m):
    gcd = get_gcd(n,m)
    r1 = n // gcd
    r2 = m // gcd
    return r1*r2*gcd

print(get_sol(n,m))