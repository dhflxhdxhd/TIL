# 04. 바닥 공사
# dp

n = int(input())
dp = [0]*n

if n < 3:
    print(n)
else:
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2]) % 796796
print(dp[-1])