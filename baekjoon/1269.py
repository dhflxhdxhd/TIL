n,m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

num = len(a-b) + len(b-a)
print(num)