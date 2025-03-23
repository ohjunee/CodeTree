n = int(input())

# Please write your code here.
def print_n_by_squre(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            if cnt > 9:
                cnt = 1
            print(cnt, end = ' ')
            cnt += 1
        print()

print_n_by_squre(n)
            