import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K= map(int,input().split()) 

weight = []
value = []    

def knapsack(i,w,v):
    global max_value
    # 무게 넘기면 종료
    if w > K:
        return
    # 최대 가치 저장
    if v > max_value:
        max_value = v
    if i == N-1: # 끝
        return 
    knapsack(i+1, w+weight[i], v+value[i])
    knapsack(i+1,w,v)
    
for _ in range(N):
    W,V = map(int, input().split())
    weight.append(W)
    value.append(V)
    
max_value = 0
knapsack(0,0,0)
print(max_value)