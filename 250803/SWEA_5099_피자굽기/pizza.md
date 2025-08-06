```python
T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
 
    waiting = [(i + 1, cheese) for i, cheese in enumerate(lst)] # 피자 번호까지 튜플로 묶어버리기
    pizza = []
 
    for _ in range(N):
        pizza.append(waiting.pop(0))  # 처음 화덕에 N개 피자 넣기
 
    # 화덕에 피자가 1개만 남을 때까지 반복
    while len(pizza) > 1:
        pizza_num, cheese = pizza.pop(0)  # 맨 앞 피자를 꺼내기
        cheese //= 2  # 치즈 반으로 나누기
 
        if cheese == 0: # 꺼내서 봤더니 치즈가 다 녹았을 때
            if waiting: # waiting 리스트가 비어있지 않는다면
                pizza.append(waiting.pop(0))  # 새로운 피자 넣어줌
            # waiting이 없다면 꺼낸 상태에서 다시 넣지 않음
        else:
            pizza.append((pizza_num, cheese))  # 다시 넣음
 
    # 마지막 피자 번호 출력
    print(f"#{test_case} {pizza[0][0]}") # 마지막으로 남은 유일한 피자의 번호
    ```