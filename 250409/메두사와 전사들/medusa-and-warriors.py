import sys
from collection import deque
from typing import List, Tuple

# 전역상수 정의
INF = int(1e9) + 10 # 무한대를 나타내는 상수

# 방향 배열: 상, 하 좌 우 (우선순위)
DX = [-1, 1, 0, 0]