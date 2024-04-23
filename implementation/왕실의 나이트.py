import sys
input = sys.stdin.readline

s = input()  # 나이트 위치, yx 로 주어진다

def solution(s):

    steps = [[2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [1, 2], [-1, -2], [1, -2]]
    
    x = int(s[1])  # x좌표
    y = int(ord(s[0])) - 96  # y좌표 , ord('a')는 97이다.

    result = 0
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
            result += 1
    return result

print(solution(s))