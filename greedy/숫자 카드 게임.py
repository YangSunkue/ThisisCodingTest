import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maxValue = int(-1e9)

for _ in range(N):
    cardList = (list(map(int, input().split())))

    minValue = min(cardList)

    maxValue = max(maxValue, minValue)

print(maxValue)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4 
# 7 3 1 8
# 3 3 3 4