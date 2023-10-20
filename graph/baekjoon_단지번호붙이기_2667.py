from collections import deque

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
    
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0 # 방문 표시 여기서 해주기
    count = 1
    while queue:
        x,y  = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0 
                queue.append((nx, ny))
                count += 1
    return count

group = []
# graph 탐색하다가 1발견하면 bfs 실행
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = bfs(i,j)
            group.append(cnt)

group.sort()
print("단지 개수: ",len(group)) # 단지가 몇개인지 출력
for cnt in group:
    print(cnt)


