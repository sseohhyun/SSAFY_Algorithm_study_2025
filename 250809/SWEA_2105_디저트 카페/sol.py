import sys
sys.stdin = open('sample_input.txt')

dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # ↘, ↙, ↖, ↗ 대각선 4방향 이동 좌표

def dfs(x, y, dir, count, dessert, start):
    global max_count
    # dir: 현재 진행 방향 인덱스(0~3), count: 방문 카페 수
    # dessert: 지금까지 먹은 디저트 종류 리스트, start: 시작 좌표

    if dir > 3:  # 방향 인덱스가 3 초과면 더 이상 진행 불가
        return

    if (x, y) == start:  # 시작점으로 돌아온 경우
        max_count = max(max_count, count)  # 최대 경로 길이 갱신
        return

    if (x, y) != start and cafe[x][y] in dessert:
        # 시작점이 아니고 이미 먹은 디저트를 또 먹으려 하면 종료
        return

    next_dessert = dessert + [cafe[x][y]]  # 현재 카페 디저트를 먹은 상태로 리스트 갱신

    # 현재 방향(dir) 그대로 이동
    nx, ny = x + dxy[dir][0], y + dxy[dir][1]
    if 0 <= nx <= N-1 and 0 <= ny <= N-1:  # 범위 체크
        dfs(nx, ny, dir, count + 1, next_dessert, start)

    # 방향을 꺾어서(dir+1) 이동
    if dir < 3:  # 마지막 방향(3)에서는 꺾을 수 없음
        nx, ny = x + dxy[dir + 1][0], y + dxy[dir + 1][1]
        if 0 <= nx < N and 0 <= ny < N:  # 범위 체크
            dfs(nx, ny, dir + 1, count + 1, next_dessert, start)

    return


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]  # 카페 지도

    max_count = -1  # 경로를 찾지 못하면 -1 출력

    # 모든 좌표에서 시작 시도
    for x in range(N):
        for y in range(N):
            # 시작점은 아래쪽 ↘↙ 대각선 진행이 가능한 위치만
            if x < N-2 and 0 < y < N-1:
                start = (x, y)  # 시작 좌표 저장
                dessert = [cafe[x][y]]  # 시작점 디저트 먹고 시작
                dfs(x+1, y+1, 0, 1, dessert, start)  # 첫 방향은 ↘

    print(f"#{test_case} {max_count}")
