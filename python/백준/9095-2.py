# 9095. 1,2,3 더하기
# dp

t = int(input())


for _ in range(t):
    n = int(input())
    dp = [0]*12 

    if n <= 2 :
        print(n)
    elif n ==3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])

    


  