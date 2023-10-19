n = int(input())

TP = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    if TP[i][0]+i <= n:
        dp[i] = max(dp[i+1],dp[i+TP[i][0]]+TP[i][1])
    else:
        dp[i] = dp[i+1]

print(dp[0])