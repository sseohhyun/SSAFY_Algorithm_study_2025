import sys
sys.stdin = open('input1.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0

# 세로로 연속된 1 길이 찾기
    for i in range(N):
        building = 0
        for j in range(M):
            if lst[i][j] == 1:
                building += 1
            else:
                if maximum < building:
                    maximum = building
                building = 0

        if maximum < building:
            maximum = building

# 가로로 연속된 1 길이 찾기
    for i in range(M):
        building = 0
        for j in range(N):
            if lst[j][i] == 1:
                building += 1
            else:
                if maximum < building:
                    maximum = building
                building = 0

        if maximum < building:
            maximum = building

    print(f'#{test_case} {maximum}')