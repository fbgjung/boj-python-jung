N = int(input())
data = []
count = 1

for _ in range(N):
    start, end = list(map(int, input().split()))
    data.append((start, end))

# 회의가 끝나는 시간으로 정렬 후 시작 시간이 빠른 순서로 정렬
data = sorted(data, key=lambda x: (x[1], x[0]))

last_end = data[0][1] # 이전 회의 종료 시간

for i in range(1,N):
    if data[i][0] >= last_end:
        count+=1
        last_end = data[i][1]
print(count)