# 1697. 숨바꼭질
from collections import deque
MAX = 10*5
sec = [0]*(MAX+1)
n, k = map(int, input().split())

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        if v == k:
            print(sec[v])
            break

        for i in (v-1, v+1, v*2):
            # 범위 안에 있고 방문하지 않았을 때
            if i < 0 or i > MAX or sec[i]:
                continue
            sec[i] = sec[v] + 1
            queue.append(i)

bfs(n)
