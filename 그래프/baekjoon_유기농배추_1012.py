import sys
sys.setrecursionlimit(10**6) # 재귀함수 한도 늘려주기
input = sys.stdin.readline
MAX = 50 + 10 # 문제에서 최대값이 50일 것이라 했기때문

#  배열 정의 (하 상 우 좌) 각각을 돌면서 내 현재위치에 더해준다. -> 상하좌우 전부 확인
dirR = [1,-1,0,0] # 행 이동 위아래
dirC = [0,0,1,-1] # 좌우

def dfs(y,x):
    graph[y][x] = False
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if graph[newY][newX]:
            dfs(newY,newX)
    
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False]* MAX for _ in range(MAX)] 

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y+1][x+1] = True # graph에 입력하는 정보가 (1,1)부터 시작하도록 함
    print("초기그래프",graph)

    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            # graph에 배추가 있고, 방문 한 적이 없다면,
            if graph[i][j]:
                dfs(i, j) # dfs 함수 호출
                answer += 1 # 지렁이를 한마리 쓰는거기 때문에
    print(answer)  # 총 필요한 지렁이 개수 출력
                