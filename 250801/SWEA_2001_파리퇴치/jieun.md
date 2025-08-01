## 2. 문제 풀이 템플릿
  ### 1) 문제 제목 - SWEA 2001
  **a. 문제 요약**
  * N x N 사이즈의 보드에 파리가 있는데 M x M 사이즈의 파리채로 쳤을 때 나오는 파리의 개수들 중 가장 큰 수를 찾는 것이다.
      
  **b. 아이디어**
  + 사용 알고리즘: 완전탐색
  + 접근 방법 요약:
      1. fly_map이라는 이중 리스트로 값을 받는다.
      2. 2중 리스트를 M 사이즈만큼 SUM을 구해서 여러가지의 SUM들 값을 받는다.
      3. MAX를 안쓰고자 results 라는 더한 값들을 모아놓은 리스트를 거꾸로 정렬하면 가장 큰 값이 맨 앞에 나오기 때문에 그 값을 반환했다.
 
  **c. 코드 (Python)**
  ```python
  def maximum_flies(fly_map,n,m) :
    # 파리의 수
    results = []

    for i in range(n-m+1):
        temp_sums = []
        for j in range(n-m+1):
            result_sum = 0
            for x in range(m) :
                for y in range(m) :
                    result_sum += fly_map[i+x][j+y]

            temp_sums.append(result_sum)
        results.extend(temp_sums)

    results.sort(reverse=True)
   # print(results)

    return results[0]


T = int(input())

for t in range(1,T+1) :
    n,m = map(int,input().split())

    fly_map = [list(map(int,input().split())) for _ in range(n)]

    #print(fly_map)
    
    print(f'#{t} {maximum_flies(fly_map,n,m)}')