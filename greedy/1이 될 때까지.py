import sys
import time
start = time.time()
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
# N이 1이 될 때까지 반복
while N != 1:
    if N % K == 0:
        N = N // K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)
end = time.time()
print(end-start)