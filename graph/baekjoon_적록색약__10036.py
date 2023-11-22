# import sys
# input = sys.stdin.readline

# N = int(input())
# graph = []

# visited = [[False] * N for _ in range(N)]

# for i in range(N):
#     graph.append(list(map(str, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# count = 0
# count2 = 0

# def dfs(x, y,color):
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N :
#             if color == "G" or color == "R":
#                 if graph[nx][ny] == "G" or graph[nx][ny] == "R":
#                     visited[nx][ny] = True
#                     dfs(nx,ny,color)
#             if color == "B":
#                 if graph[nx][ny] == "B":
#                     visited[nx][ny] = True
#                     dfs(nx,ny,color)
                    
# def dfs2(x, y,color):
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N :
#             if color == "G" and graph[nx][ny] == "G": 
#                 visited[nx][ny] = True
#                 dfs2(nx,ny,color)
#             if color == "B" and graph[nx][ny] == "B":
#                 visited[nx][ny] = True
#                 dfs2(nx,ny,color)
#             if color == "R" and graph[nx][ny] == "R":
#                 visited[nx][ny] = True
#                 dfs2(nx,ny,color)
                    
# for i in range(N):
#     for j in range(N):
#         if visited == False:
#             count += 1
#             dfs(i,j,graph[i][j])

            
# visited = [[False] * N for _ in range(N)]

 
# for i in range(N):
#     for j in range(N):
#         if visited == False:
#             count2 += 1
#             dfs2(i,j,graph[i][j])
        
# print(count,count2)

import sys
input = sys.stdin.readline

N = int(input())
graph = []

visited = [[False] * N for _ in range(N)]

for i in range(N):
    graph.append(list(map(str, input())))  # rstrip()을 추가하여 줄 바꿈 문자를 제거합니다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
count2 = 0

def dfs(x, y, color):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if color == "G" or color == "R":
                if graph[nx][ny] == "G" or graph[nx][ny] == "R":
                    visited[nx][ny] = True
                    dfs(nx, ny, color)
            if color == "B":
                if graph[nx][ny] == "B":
                    visited[nx][ny] = True
                    dfs(nx, ny, color)

def dfs2(x, y, color):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if (color == "G" and graph[nx][ny] == "G") or (color == "R" and graph[nx][ny] == "R") or (color == "B" and graph[nx][ny] == "B"):
                visited[nx][ny] = True
                dfs2(nx, ny, color)
                    
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            dfs(i, j, graph[i][j])

# visited 초기화
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count2 += 1
            dfs2(i, j, graph[i][j])

print(count2, count)
