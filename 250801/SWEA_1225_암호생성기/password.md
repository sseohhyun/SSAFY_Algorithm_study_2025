```python
def cycle(lst):                     # 한 사이클을 정의
    for i in range(1, 6):           # 한 사이클은 5번 수행
        new_val = lst[0] - i        # i번째 수행은 첫 원소에서 i를 빼는 것
        if new_val <= 0:            # i를 뺀 값이 0 이하라면
            lst[0] = 0              # 첫 원소를 0으로 바꾸고
            a = lst.pop(0)          # pop
            lst.append(a)           # 리스트 맨뒤로 옮김
            break                   # 암호 완성
        else:
            lst[0] = new_val
            a = lst.pop(0)
            lst.append(a)
 
    return lst
 
for i in range(1, 11):              # 10개의 테스트 케이스
    tc = int(input())
    num_list = list(map(int,input().split()))
    last_val = num_list[-1]         # last_val 정의
 
    while last_val != 0:            # last_val이 0이 될 때까지
        num_list = cycle(num_list)  # cycle을 반복 수행
        last_val = num_list[-1]     # last_val 최신화
 
    # print(f'{tc} {*num_list}') f-string 안에서 unpacking 불가능
    print(f'#{tc}', *num_list)
    ```