  ## 1) 파리 퇴치 - SWEA 2001
  **a. 문제 요약**
  + 목적: 1회 타격으로 최대한 많은 파리 죽이기
  + 조건: N*N 범위에서 M*M 크기의 파리채로 1회 타격
  + 입력: T = 테스트케이스, N = 전체 범위, M = 파리채 크기
  + 출력: #{테스트케이스} {죽인 파리 수}
      
  **b. 아이디어**
  + 사용 알고리즘:
  + 접근 방법 요약:
      1. 5중 반복으로 시도
      2. 의외로 시간초과가 안남
      3. 여유 되면 누적합으로 다시 풀어보면 좋을 듯 하다
      4. 안된다
 
  **c. 코드 (Python)**
    ```python
    T = int(input())
    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        area = [list(map(int, input().split())) for _ in range(N)]
     
        mx = 0
        for x in range(N-M+1):
            for y in range(N-M+1):
                sm = 0
                for i in range(M):
                    for j in range(M):
                        sm += area[x+i][y+j]
                mx = max(sm, mx)
     
        print(f"#{test_case} {mx}")
    ```
    ```