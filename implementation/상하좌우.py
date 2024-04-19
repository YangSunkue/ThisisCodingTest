import sys
input = sys.stdin.readline

N = int(input())
command = list(input().split())

#  갈 수 있는지 판단하는 함수
def goingNoGoing(x, y):
    if 1 <= x <= N and 1 <= y <= N:
        return True
    return False
    
# 좌표 계산을 위한 변수들
moveType = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 좌표는 1,1 부터 시작
x = 1
y = 1
for i in command:  # 경로를 하나씩 대입
    # L R U D 중 하나에 맞춰, 갈 수 있을 경우 좌표를 바꾼다
    for j in range(len(moveType)):
        if i == moveType[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            if goingNoGoing(nx, ny):
                x = nx
                y = ny
                break
            else: break
            
print(f'{x} {y}')


# 5
# R R R U D D