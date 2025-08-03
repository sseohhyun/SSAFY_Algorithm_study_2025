# SSAFY_Algorithm_study_2025

## 2. 문제 풀이 템플릿
  ### 1) 문제 제목 - SWEA XXXX
  **a. 문제 요약**
  + 목적: (문제에서 요구하는 것)
  + 조건: (제약 조건 정리)
  + 입력: (예시 입력 정리)
  + 출력: (예시 출력 정리)
      
  **b. 아이디어**
  + 사용 알고리즘: (예: BFS, 완전탐색 등)
  + 접근 방법 요약:
      1. (입력 파싱)
      2. (조건 확인)
      3. (반복문 / 재귀 호출 설명)
 
  **c. 코드 (Python)**
    ```python
      코드 작성
    ```

---

## 3. 스터디 정리 템플릿
  ### 1) 문제 제목 - SWEA XXXX
  **a. 문제 요약**
  + 난이도: D2 / D3 / D4
  + 알고리즘 분류: (예: DFS, 시뮬레이션 등)  
      
  **b. 문제풀이 아이디어 요약**
  + 핵심 아이디어
  + 자료구조/기법
  + 코드 요약
 
  **c. 코드 요약**
    ```python
      import sys
      sys.stdin = open("input_2805.txt", "r")

      T = int(input())
      for t_c in range (1, T+1):
          N = int(input())
          arr = [list(map(int, input())) for _ in range(N)]

          n = N // 2 # 가운데를 나타낼 인덱스
          get_sum = 0 # 최종 결과 : 농작물의 가치의 총합

          for i in range(N):
              if i <= n:
                  for j in range(n-i, n+i+1):
                      get_sum += arr[i][j]
              else:
                  for j in range(i-n, N-i+n):
                      get_sum += arr[i][j]
          
          print(f'#{t_c} {get_sum}')  
    ``` 
