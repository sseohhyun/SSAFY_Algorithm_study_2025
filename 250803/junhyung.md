  ## 1) 피자 굽기 - SWEA 5099
  **a. 문제 요약**
  + 목적: 가장 마지막에 완성되는 피자의 번호
  + 조건: 피자 위의 치즈가 다 녹아야 완성, 화덕 넓이의 제한
  + 입력: T = 테스트케이스, N = 화덕의 넓이, M = 구워야 하는 피자의 수
  + 출력: #{테스트케이스} {마지막 피자의 번호}
      
  **b. 아이디어**
  + 사용 알고리즘: deque
  + 접근 방법 요약:
      1. 구워야 하는 피자와 화덕을 리스트로 만들어 다중탐색하면 가능할 것 같다.
      2. 다만 필요한 연산량이 많아 시간이 될 지 불확실하다.
      3. 스택/큐 에 들어있는 문제이다.
      4. 큐 쪽으로 접근하는 것이 옳아 보인다.
      5. 일반적인 큐가 아니라 원형으로 연결된 큐가 필요해 보인다.
      6. rotate() 메서드를 통해 원형으로 돌릴 수 있다.
      7. 코드를 짜고 보니 계산은 의도한 대로 작동하나 피자에 인덱싱을 하지 않아 목표한 출력을 할 수 없다.
      8. 큐를 생성할 때 값 하나 대신 튜플을 넣어서 생성한다.
 
  **c. 코드 (Python)**
    ```python
    import sys
    sys.stdin = open('sample_input.txt')

    from collections import deque

    T = int(input())
    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        pizza_input = list(map(int, input().split()))

        pizza = deque((i + 1, cheese) for i, cheese in enumerate(pizza_input))  # 피자번호, 치즈양
        oven = deque()

        for _ in range(N):  # 화덕에 피자 투입
            oven.append(pizza.popleft())

        while len(oven) > 1:    # 피자가 한 개 남을 때까지
            num, cheese = oven.popleft()
            cheese //= 2  # 치즈 절반으로

            if cheese == 0:
                if pizza:
                    oven.append(pizza.popleft())
            else:
                oven.append((num, cheese))

        print(f"#{test_case} {oven[0][0]}") # 남은 마지막 피자 번호
    ```