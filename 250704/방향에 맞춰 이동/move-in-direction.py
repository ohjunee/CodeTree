n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# dist = [3, 2, 1, 2]
# dir = [N, E, S, E]
# Please write your code here.
cur_x, cur_y = 0,0
for idx in range(n):
    if dir[idx] == 'E':
        cur_x += dx[0]*dist[idx]
        cur_y += dy[0]*dist[idx]
    if dir[idx] == 'S':
        cur_x += dx[1]*dist[idx]
        cur_y += dy[1]*dist[idx]
    if dir[idx] == 'W':
        cur_x += dx[2]*dist[idx]
        cur_y += dy[2]*dist[idx]
    if dir[idx] == 'N':
        cur_x += dx[3]*dist[idx]
        cur_y += dy[3]*dist[idx]
print(f"{cur_x} {cur_y}")
    