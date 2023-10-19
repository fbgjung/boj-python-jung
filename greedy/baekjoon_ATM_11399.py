N = int(input())
p = list(map(int, input().split()))

p.sort()

result = 0

answer = []

for i in p:
    print("i: ",i)
    result += i
    answer.append(result)
        
print(sum(answer))

    