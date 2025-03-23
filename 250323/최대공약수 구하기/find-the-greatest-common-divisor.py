n, m = map(int, input().split())

# Please write your code here.
def get_maximum_dividen(n, m):
    a = max(n, m)
    b = min(n, m)
    if a % b:
        r = a % b
        return get_maximum_dividen(b, r)
    else:
        return b

print(get_maximum_dividen(n, m))