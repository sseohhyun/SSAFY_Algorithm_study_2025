import sys
sys.stdin = open('sample_input.txt')

# 최대 전원 연결 코어 + 최소 전선 길이
# 코어의 위치를 배열로 만든 뒤 테두리에 있는 코어 제외 - 앞으로의 계산에 필요없음 - 최적화
# 테두리 제거한 배열을 DFS
# DFS 에서 상하좌우+패스 5가지 방향 보내기
# 상하좌우에서 전선 설치할 WIRE
# 설치 과정에서 장애물이 있을 경우 전선 회수
# 끝까지 설치했을 경우 회수하지 않고 연결된 코어 수 +1, 전선 길이 리턴
# DFS 에서 전원 연결 수 + 전선 길이 리턴하여 max(data, key=lambda x: (연결 코어 수, -전선 길이)) 활용

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하, 상, 우, 좌 방향 벡터

def dfs(idx, plugged, sum_wire):
    """
    idx: 현재 처리 중인 core의 인덱스
    plugged: 지금까지 전원에 연결된 코어 개수
    sum_wire: 지금까지 설치한 전선 길이 합
    """
    global max_plugged, min_wire

    # 모든 core를 다 처리한 경우
    if idx >= len(core):
        # 더 많은 코어 연결에 성공한 경우 → min_wire 갱신
        if plugged > max_plugged:
            max_plugged = plugged
            min_wire = sum_wire
        # 같은 개수의 코어를 연결했지만 전선이 더 짧으면 갱신
        elif plugged == max_plugged:
            min_wire = min(min_wire, sum_wire)
        return

    x, y = core[idx]  # 현재 코어 위치

    # 4방향으로 전선 설치 시도
    for dir in range(4):
        success, length = wire(x, y, dir)
        if success:
            dfs(idx + 1, plugged + 1, sum_wire + length)  # 연결 성공 시 다음 코어로 진행
            # 백트래킹: 설치했던 전선 제거
            cx, cy = dxy[dir]
            nx, ny = x + cx, y + cy
            for _ in range(length):
                area[nx][ny] = 0
                nx += cx
                ny += cy

    # 해당 코어를 연결하지 않고 넘어가는 경우
    dfs(idx + 1, plugged, sum_wire)


def wire(x, y, dir):
    """
    (x, y) 위치의 코어에서 dir 방향으로 전선을 설치 시도
    성공 시 (True, 전선 길이), 실패 시 (False, 0) 반환
    """
    cx, cy = dxy[dir]
    nx, ny = x + cx, y + cy
    path = []  # 설치한 전선 좌표 기록

    while 0 <= nx < N and 0 <= ny < N:
        if area[nx][ny] != 0:  # 다른 코어나 전선이 있으면 실패
            # 설치했던 전선 제거 후 실패 반환
            for px, py in path:
                area[px][py] = 0
            return False, 0
        area[nx][ny] = 2  # 전선 설치
        path.append((nx, ny))
        nx += cx
        ny += cy

    # 경계까지 도달 시 성공
    return True, len(path)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    # 테두리(가장자리)에 있는 코어는 이미 연결된 것으로 간주하므로 제외
    core = []
    for x in range(N):
        for y in range(N):
            if area[x][y] == 1 and x not in (0, N-1) and y not in (0, N-1):
                core.append((x, y))

    max_plugged, min_wire = 0, float('inf')
    dfs(0, 0, 0)
    print(f"#{test_case} {min_wire}")


# dxy = [(1,0), (-1, 0), (0, 1), (0, -1)]
#
# def dfs(idx, plugged, sum_wire): # 현재 코어 순서, 연결된 코어 수, 누적 전선 길이
#     global max_plugged, min_wire
#     if plugged + len(core) - idx < max_plugged:
#         return
#     if idx >= len(core):    # 마지막 코어에 도착. -> 현재 값이 최대 전원 연결 수인지 + 최소 전선 길이인지
#         max_plugged = max(max_plugged, plugged)
#         min_wire = min(min_wire, sum_wire)
#         return
#
#     nx, ny = core[idx]
#
#     if area[nx+1][ny] == 0:
#         # wire 호출 + 리턴값으로 plug, len_wire 값 변경 -> dfs 출발 -> 변경된 값 백트래킹
#         now_wire = 0
#         if wire(nx-1, ny, now_wire, 0):
#             dfs(idx+1, plugged+1, sum_wire)
#         else:
#             dfs(idx+1, plugged, sum_wire)
#     if area[nx-1][ny] == 0:
#         now_wire = 0
#         if wire(nx-1, ny, now_wire, 1):
#             dfs(idx+1, plugged+1, sum_wire)
#         else:
#             dfs(idx+1, plugged, sum_wire)
#     if area[nx][ny-1] == 0:
#         now_wire = 0
#         if wire(nx-1, ny, now_wire, 2):
#             dfs(idx+1, plugged+1, sum_wire)
#         else:
#             dfs(idx+1, plugged, sum_wire)
#     if area[nx][ny+1] == 0:
#         now_wire = 0
#         if wire(nx-1, ny, now_wire, 3):
#             dfs(idx+1, plugged+1, sum_wire)
#         else:
#             dfs(idx+1, plugged, sum_wire)
#     dfs(idx+1, plugged, sum_wire)    # wire 없이 다음 idx 로 dfs
#
# def wire(x, y, now_wire, dir): # 각 방향으로 와이어 연결 시도 - dir 방향으로 진행 -> 끝까지 도달 시 True 리턴 -> 도달 실패 시 전선 지우며 백트래킹 + False 리턴
#     if x in (0, N-1) or y in (0, N-1):
#         now_wire += 1
#         return True
#
#     cx, cy = dxy[dir]
#     nx, ny = x + cx, y + cy
#     if area[nx][ny] == 0:
#         area[nx][ny] = 2
#         if wire(nx, ny, now_wire+1, dir):
#             return
#         area[nx][ny] = 0
#     else:
#         return False
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     area = [list(map(int, input().split())) for _ in range(N)]
#
#     core = []   # 코어의 위치를 기억할 인덱스 -> 이를 기반으로 dfs 돌아갈 예정
#     for x in range(N):
#         for y in range(N):
#             if area[x][y] == 1 and x not in (0, N-1) and y not in (0, N-1): # 테두리 코어 제외한 나머지 코어 입력
#                 core.append((x, y))
#
#     max_plugged, min_wire = 0, 200
#
#     dfs(0, 0, 0)
#
#     print(f"#{test_case} {min_wire}")