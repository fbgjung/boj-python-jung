T = int(input())
N = []

for i in range(T):
    n = int(input())
    N.append(n)
    
dp = [0] * (max(N)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
   
for i in range(4,max(N)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in N:
    print(dp[n])

    
