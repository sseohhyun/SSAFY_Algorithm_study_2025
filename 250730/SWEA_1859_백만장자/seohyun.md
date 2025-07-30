## 2. 문제 풀이 템플릿
  ### 1) 문제 제목 - SWEA 1859
  **a. 문제 요약**
  + 목적: (문제에서 요구하는 것)
  + 조건: (제약 조건 정리)
  + 입력: (예시 입력 정리)
  + 출력: (예시 출력 정리)
      
  **b. 아이디어**
  + 사용 알고리즘: 
  + 접근 방법 요약:
      1. 리스트에서 해당 인덱스를 기준으로 그 인덱스보다 큰 값들 중에서 max값을 찾음
      2. max 값과 해당 인덱스를 비교해 만약에 해당 인덱의 값이 더 크거나 같다면 pass
      3. 그외의 경우엔 차이 만큼 누적함
 
  **c. 코드 (Python)**
    ```python
    T = int(input())
    for t_c in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        mx = 0
        for j in range(i+1,n):
            if mx <= lst[j]:
                mx = lst[j]
        # mx = max(lst[i+1:n])

        if lst[i] >= mx:
            pass
        else:
            ans += mx - lst[i]

    print(f'#{t_c} {ans}')
    ```