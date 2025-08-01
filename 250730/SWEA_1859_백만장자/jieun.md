## SWEA 1859 백만장자
 **a. 문제 요약**
  * 값이 예측된 날에서 원재를 사재기하기 위한 최대의 이익 값을 찾는다.
      
  **b. 아이디어**
  + 사용 알고리즘:
  + 접근 방법 요약:
      1. 연속된 N일 동안 물건을 사야하는줄 알았으나 사는것은 자유고 N일 동안의 물건의 매매가를 예측한다는 것
      2. 무조건 맨 마지막 날에 판다는 조건이면 고민할 필요가 없겠지만 MAX의 수치는 인덱스가 올라감에 따라 언제든지 바뀔 수 있다.
      3. 예를 들어 1 1 3 1 2인 경우 첫째 둘째날 사서 셋째날에 파는게 이득인데 문제는 그후로 4일째에 한번 더 사고 5일째에는 팔아야한다.
      4. 그렇기 때문에 무조건 팔아야 하는 마지막 날을 기준으로 하기 위해 예측된 날짜를 뒤집에서 또 하나의 리스트로 만든다.
      5. 그럼 이제 1 1 3 1 2 에서의 예제는 뒤집은 값이 2 1 3 1 1 이 된다.
      그리고 맨 첫 값을 MAX로 잡는다.
      6. 인덱스가 올라가면서 MAX값보다 작은 값이 나오면 TOTAL 이익에 (MAX-MAX보다작은값) 더해준다. 만일 다음값이 MAX보다 크다면 MAX는 바뀐다.
 
  **c. 코드 (Python)**

    ```python
    T = int(input())

    for t in range(1,T+1) :
        n = int(input())
        price_list = list(map(int,input().split()))
     
     reversed_price = price_list[::-1]
     max = reversed_price[0]
     total = 0

     for price in reversed_price :
          if price > max :
               max = price 
               continue
          total += (max - price)
     print(f"#{t} {total}")
