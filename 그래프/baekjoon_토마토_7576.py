from collections import deque
m,n = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()

# 익은 토마토를 찾아서 bfs 시작
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 모든 익은 토마토에 대해 bfs를 시작해야 한다
            # bfs(i,j)
            queue.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == -1:
                continue
            # 인접한 토마토를 익게한다.
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1

result = 0
for i in range(n):
    for j in range(m):
        # 안 익은 토마토 있으면 -1 출력하고 프로그램 종료
        if graph[i][j] == 0:
            print(-1)
            exit(0) # break 아닙니다!!!!!!!!!
        result = max(result, graph[i][j] - 1)
print(result)



