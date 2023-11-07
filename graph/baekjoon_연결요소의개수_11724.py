import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 노드 수, 간선 수
graph = [[] for _ in range(n+1)]
visited = [False] * (n*1)
count = 0

for _ in range(m):
    a,b = map(int, input().split())
    # 노드 간 양방향 연결
    graph[a].append(b)
    graph[b].append(a)
    
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
    
# dfs 실행
def dfs(node):
    visited[node] = True # 해당 노드를 방문처리
    for i in graph[node]: # 현재 노드와 연결된 이웃 노드 방문
        if not visited[i]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
        
print(count)