import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort(reverse=True)

result = 0

# 큰 수가 더해지는 횟수 / 반복되는 수열 갯수를 구해 K를 곱하고, 나머지 갯수만큼 큰 수를 더해주면 된다
big = int(M / (K + 1)) * K + M % (K + 1)
# 작은 수가 더해지는 횟수 / 반복되는 수열 갯수만큼만 작은 수가 등장한다
small = int(M / (K + 1))

result += numList[0] * big
result += numList[1] * small

print(result)