#단어정렬
import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

arr = list(set(arr))

arr.sort(key=lambda x : len(x))

for a in arr:
    print(a)