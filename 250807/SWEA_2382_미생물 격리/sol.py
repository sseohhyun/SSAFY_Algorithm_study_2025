import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    # N: 셀 크기, M: 격리 시간, K: 미생물 군집 수

    area = [[None] * N for _ in range(N)]
    # 격자판 초기화 (미생물이 없는 곳은 None)

    for _ in range(K):
        r, c, count, direct = map(int, input().split())
        area[r][c] = [count, direct]
        # 미생물 정보 입력 (개수, 방향)

    for _ in range(M):  # M시간 동안 시뮬레이션
        future = [[None] * N for _ in range(N)]
        # 다음 시간의 상태를 저장할 임시 격자판

        for x in range(N):
            for y in range(N):
                if area[x][y] is None:
                    continue  # 미생물이 없으면 건너뛰기

                count, direction = area[x][y]

                # 방향에 따라 이동 좌표 계산
                if direction == 1:
                    nx, ny = x - 1, y  # 상
                elif direction == 2:
                    nx, ny = x + 1, y  # 하
                elif direction == 3:
                    nx, ny = x, y - 1  # 좌
                else:
                    nx, ny = x, y + 1  # 우

                # 약품이 놓인 가장자리면 수 감소 및 방향 반전
                if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                    count //= 2  # 절반으로 줄기
                    if count == 0:
                        continue  # 0이면 사라짐
                    # 방향 반전
                    if direction == 1:
                        ndir = 2
                    elif direction == 2:
                        ndir = 1
                    elif direction == 3:
                        ndir = 4
                    else:
                        ndir = 3
                else:
                    ndir = direction  # 방향 유지

                # 이미 미래 격자에 다른 미생물이 있으면
                if future[nx][ny] is not None:
                    # 더 큰 군집이 오면 방향 갱신
                    if future[nx][ny][2] < count:
                        future[nx][ny][1] = ndir
                        future[nx][ny][2] = count
                    future[nx][ny][0] += count  # 개수 누적
                else:
                    # 처음 오는 미생물: [총합, 방향, 비교용 최대값]
                    future[nx][ny] = [count, ndir, count]

        # 비교용 최대값은 제거하고 [개수, 방향]만 남김
        for x in range(N):
            for y in range(N):
                if future[x][y] is not None:
                    future[x][y] = [future[x][y][0], future[x][y][1]]

        area = future  # 현재 상태 업데이트

    # 전체 미생물 수 계산
    total = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] is not None:
                total += area[i][j][0]

    print(f"#{test_case} {total}")

'''
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    area = [[None] * N for _ in range(N)]

    for _ in range(K):
        r, c, count, direct = map(int, input().split())
        area[r][c] = [count, direct]

    for _ in range(M):
        future = [[None] * N for _ in range(N)]

        for x in range(N):
            for y in range(N):
                if area[x][y] is None:
                    continue
                direction = area[x][y][1]

                if direction == 1:  # 위: (x-1, y)
                    nx, ny = x - 1, y
                elif direction == 2:  # 아래: (x+1, y)
                    nx, ny = x + 1, y
                elif direction == 3:  # 좌: (x, y-1)
                    nx, ny = x, y - 1
                else:  # direction == 4, 우: (x, y+1)
                    nx, ny = x, y + 1

                if future[nx][ny] is not None:
                    if area[x][y][0] > future[nx][ny][0]:
                        future[nx][ny][1] = area[x][y][1]
                        future[nx][ny][0] += area[x][y][0]
                    else:
                        future[nx][ny][0] += area[x][y][0]
                else:
                    future[nx][ny] = area[x][y]

                # 레드존(경계) 처리
                if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                    future[nx][ny][0] //= 2
                    if future[nx][ny][1] == 1:
                        future[nx][ny][1] = 2
                    elif future[nx][ny][1] == 2:
                        future[nx][ny][1] = 1
                    elif future[nx][ny][1] == 3:
                        future[nx][ny][1] = 4
                    elif future[nx][ny][1] == 4:
                        future[nx][ny][1] = 3

        area = future

    total = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] is not None:
                total += area[i][j][0]

    print(f"#{test_case} {total}")
'''