from collections import deque
import sys

queue = deque([])

n = int(input())
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(int(cmd[-1]))
    
    elif cmd[0] == "pop":
        print(queue.popleft() if queue else -1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        print(0 if queue else 1)
        
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)

    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)
