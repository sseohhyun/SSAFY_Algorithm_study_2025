## 2. 문제 풀이 템플릿
  ### 1) 문제 제목 - SWEA 2001
  **a. 문제 요약**
  + 목적: (문제에서 요구하는 것)
  + 조건: (제약 조건 정리)
  + 입력: (예시 입력 정리)
  + 출력: (예시 출력 정리)
      
  **b. 아이디어**
  + 사용 알고리즘: 완전탐색
  + 접근 방법 요약:
      1. 모든 지점을 다 돈다.
      2. m만큼 또 반복해서 각 지점을 sum_temp에 더해둔다.
      3. 더한 값을 리스트에 넣고 최종적으로 리스트에서 최대값을 찾는다.
 
  **c. 코드 (Python)**
    ```python
    T = int(input())
    for t_c in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]


    sum_list = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_temp = 0
            for k in range(m):
                for s in range(m):
                    sum_temp += arr[i+k][j+s]
            sum_list.append(sum_temp)

    max_sum = max(sum_list)

    print(f'#{t_c} {max_sum}')
    ```