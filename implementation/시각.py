import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(0, N + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            sstr = str(i) + str(j) + str(k)
            if '3' in sstr:
                cnt += 1

print(cnt)