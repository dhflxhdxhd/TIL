# 11053. 가장 긴 증가하는 부분 수열
# dp

n = int(input())
nums = list(map(int,input().split()))
dp = [1] * (n)


for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1) 



print(max(dp))
