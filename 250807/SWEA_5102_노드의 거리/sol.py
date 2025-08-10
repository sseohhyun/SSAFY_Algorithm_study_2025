# 방향성 없는 그래프를 위한 인접 리스트 생성 함수
def build_인접리스트(간선, 노드개수):
    인접리스트 = {i: [] for i in range(1, 노드개수 + 1)}
    for node1, node2 in 간선:
        # 양방향 간선 추가
        인접리스트[node1].append(node2)
        인접리스트[node2].append(node1)
    return 인접리스트


# BFS를 이용한 최단 거리 탐색 함수
def BFS(인접리스트, 시작점, 도착점, 노드개수):
    # 노드 번호가 1부터 시작하므로 노드개수+1 크기로 설정
    방문기록 = [0] * (노드개수 + 1)
    거리기록 = [0] * (노드개수 + 1)
    queue = []

    # 출발 노드 설정
    queue.append(시작점)
    방문기록[시작점] = 1
    거리기록[시작점] = 0

    while queue:
        현재노드 = queue.pop(0)  # 조사해야할 노드는 큐에 저장돼있으니, 하나씩 꺼내 조사한다

        # 도착 노드에 도달하면 거리 반환
        if 현재노드 == 도착점:
            return 거리기록[현재노드]

        # 현재 노드의 이웃들을 탐색
        for neighbor in 인접리스트[현재노드]:  # 현재노드가 이동할 수 있는 노드들을 하나씩 순회
            if not 방문기록[neighbor]:
                방문기록[neighbor] = 1
                거리기록[neighbor] = 거리기록[현재노드] + 1
                queue.append(neighbor)

    # 도착 노드에 도달할 수 없을 경우 0 반환
    return 0

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    노드개수, 간선개수 = map(int, input().split())
    간선 = [list(map(int, input().split())) for _ in range(간선개수)]
    시작점, 도착점 = map(int, input().split())

    인접리스트 = build_인접리스트(간선, 노드개수)
    result = BFS(인접리스트, 시작점, 도착점, 노드개수)

    print(f"#{test_case} {result}")