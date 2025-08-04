  ## 1) 미생물 격리 - SWEA 2382
  **a. 문제 요약**
  + 목적: M 만큼의 시간이 지난 뒤 살아있는 미생물 수의 합
  + 조건: 영역의 테두리 부분에 도착하면 절반이 죽고 방향이 바뀐다, 여러 미생물들이 만나면 가장 큰 미생물 무리를 기준으로 합쳐진다
  + 입력: T = 테스트케이스, N = 구역의 한 변, M = 격리 시간, K = 미생물 군집의 수
  + 출력: #{테스트케이스} {남은 미생물의 수}
      
  **b. 아이디어**
  + 사용 알고리즘:
  + 접근 방법 요약:
      1. 
 
  **c. 코드 (Python)**
    ```python
    T = int(input())
    for test_case in range(1, T + 1):
        N, M, K = map(int, input().split())

        area = [[None] * N for _ in range(N)]
        for _ in range(K):
            r, c, count, direction = map(int, input().split())
            area[r][c] = [count, direction]

        for _ in range(M):
            # future: 다음 타임스텝의 상태 저장
            future = [[None] * N for _ in range(N)]

            for x in range(N):
                for y in range(N):
                    if area[x][y] is None:
                        continue

                    count, direction = area[x][y]
                    # 방향에 따라 다음 위치로 이동
                    if direction == 1:   # 위
                        nx, ny = x - 1, y
                    elif direction == 2: # 아래
                        nx, ny = x + 1, y
                    elif direction == 3: # 좌
                        nx, ny = x, y - 1
                    else:                # 우
                        nx, ny = x, y + 1

                # 경계선 도착 시 처리
                    crossed_border = nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1
                    if crossed_border:
                        count //= 2  # 미생물 절반 소멸
                        if count == 0:
                            continue  # 군집 소멸: future에 기록하지 않음
                        # 방향 반전
                        if direction == 1:
                            new_direction = 2
                        elif direction == 2:
                            new_direction = 1
                        elif direction == 3:
                            new_direction = 4
                        else:
                            new_direction = 3
                    else:
                        new_direction = direction

                    # 미래 위치에 군집이 이미 있으면 병합 처리 필요!
                    if future[nx][ny] is not None:
                        # 가장 큰 군집이 방향 결정: [총합, 방향, 최대수]
                        if future[nx][ny][2] < count:
                            future[nx][ny][1] = new_direction  # 방향 업데이트
                            future[nx][ny][2] = count
                        future[nx][ny][0] += count  # 미생물 수 합산
                    else:
                        # [미생물수, 방향, 현재최대]
                        future[nx][ny] = [count, new_direction, count]

            # 미래 area 갱신: [미생물수, 방향] 형식으로 깔끔히 정제
            for x in range(N):
                for y in range(N):
                    if future[x][y] is not None:
                        future[x][y] = [future[x][y][0], future[x][y][1]]

            area = future  # 다음 타임스텝으로 이동

        # 전체 미생물 수 합산
        total_microbes = 0
        for i in range(N):
            for j in range(N):
                if area[i][j] is not None:
                    total_microbes += area[i][j][0]

        print(f"#{test_case} {total_microbes}")
    ```