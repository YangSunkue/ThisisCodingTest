import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # 배열 크기, 총 더하는 횟수, 연속으로 더할 수 있는 횟수

# 숫자 받아서 내림차순 정렬
numList = []
for i in list(map(int, input().split())):
    numList.append(i)
numList.sort(reverse=True)

cnt = 0  # 더한 횟수 저장할 변수
result = 0  # 결과값 저장할 변수

while(cnt < M):
    for _ in range(K):  # 가장 큰 수 K번 더하기
        if cnt < M:
            result += numList[0]
            cnt += 1

    
    if cnt < M:
        result += numList[1]  # 두번째로 큰 수 1번 더하기
        cnt += 1

print(result)


# 5 8 3
# 2 4 5 4 6