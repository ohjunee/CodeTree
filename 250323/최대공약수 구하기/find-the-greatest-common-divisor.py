n, m = map(int, input().split())

# Please write your code here.
def get_maximum_dividen(n, m):
    for i in range(1, min(n, m)+1, 1):
        if n % i == 0 and m % i == 0:
            res = i
    return res
print(get_maximum_dividen(n, m))