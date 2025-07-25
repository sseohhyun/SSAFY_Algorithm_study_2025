  ## 1) 백만 장자 프로젝트 - SWEA 1859
  **a. 문제 요약**
  + 목적: N일간의 기간 내 최대 이득
  + 조건: 구매는 1일1회, 판매는 자유
  + 입력: T = 테스트케이스, N = 거래 날의 수, N개의 자연수
  + 출력: #{테스트케이스} {최대 이익}
      
  **b. 아이디어**
  + 사용 알고리즘:
  + 접근 방법 요약:
      1. 실제 상황을 상상한다
      2. 장바구니 리스트를 생성하여 남은 N들 중 가장 큰 값을 만날 경우 판매
      3. 남은 N들 중 가장 큰 값을 찾는 데에 오래 걸릴 것 같음
      4. 장바구니 리스트 필요없이 판매 했다 치고 넘어가기
      5. 3번은 추가 고민 필요
      6. 시간 초과 (7/10)
      7. 2중 반복문 해제할 방법 필요
      8. 해제 방법 못찾음 -> 대신 최소한으로 할 수 있도록 함
 
  **c. 코드 (Python)**
    ```python
    T = int(input())
    for test_case in range(1, T + 1):
      N = int(input())
      lst = list(map(int, input().split()))
      sum = 0
      
      for i in range(N):
        nextMax = -1
        nextMax = max(lst[i:])
        if lst[i] < nextMax:
          sum += nextMax - lst[i]
          
      print(f"#{test_case} {sum}")
    ```
    ```python
    T = int(input())
    for test_case in range(1, T + 1):
      N = int(input())
	    lst = list(map(int, input().split()))
	    sum = 0
	
	    nextMax = lst[0]
	    for i in range(N):
		    if lst[i] == nextMax and i < N-1:
			    nextMax = max(lst[i+1:])
		    if lst[i] < nextMax:
			    sum += nextMax - lst[i]

	    print(f"#{test_case} {sum}")
    ```
    ```