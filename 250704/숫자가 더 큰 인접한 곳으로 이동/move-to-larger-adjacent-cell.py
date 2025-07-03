n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cur_x, cur_y = r, c

def isInRange(x, y, n):
    if x < 1 or y < 1:
        return False
    elif x >= n or y >= n:
        return False
    else:
        return True
ret = []
cur_val = a[cur_x][cur_y]
cnt = 0
ret.append(cur_val)
while True:
    for i in range(n):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        cnt += 1
        if not isInRange(next_x, next_y, n):
            continue
        if a[next_x][next_y] > cur_val:
            cur_x, cur_y = next_x, next_y
            cur_val = a[next_x][next_y]
            ret.append(cur_val)
            cnt = 0
    if cnt == 4:
        break
print(*ret)
