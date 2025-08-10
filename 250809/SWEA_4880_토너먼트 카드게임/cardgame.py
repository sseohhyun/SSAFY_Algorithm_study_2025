import sys
sys.stdin = open('sample_input.txt')

# key가 value를 이김
play = {
    1: 3,   # 가위(1)는 보(3)를 이김
    2: 1,   # 바위(2)는 가위(1)를 이김
    3: 2    # 보(3)는 바위(2)를 이김
}

def rsp(lst):
    # 앞 번호가 이기거나 비기는 경우, 앞 번호 학생 반환
    if play[lst[0][1]] == lst[1][1] or lst[0][1] == lst[1][1]:
        return lst[0]
    # 뒷 번호 학생 반환
    else:
        return lst[1]

def find_winner(start, end):
    # 그룹에 학생이 한 명만 남은 경우 해당 학생 반환
    if start == end:
        return students[start]

    mid = (start + end) // 2 # 그룹을 두 개로 나누기

    # 재귀 호출
    winner1 = find_winner(start, mid)
    winner2 = find_winner(mid + 1, end)

    # 두 사람을 리스트에 담아 가위바위보
    return rsp([winner1, winner2])

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    students = []

    for idx, value in enumerate(cards):     # 학생 리스트를 (번호, 카드) 튜플 형태로 만들기
        students.append((idx + 1, value))   # 학생 번호는 1부터 시작

    final_winner = find_winner(0, N - 1)

    print(f'#{test_case} {final_winner[0]}')

'''
[재귀 작동 방식 설명]

학생 0,1,2,3 있다고 가정
처음에 find_winner 하면 
winner1 = find_winner(0,1)
    - 재귀호출로 인해 winner1 = 학생 0, winner2 = 학생 1로 나눠지고, 가위바위보를 하게됨.
    - 가위바위보 승자가 결승전의 winner1이 됨

winner2 = find_winner(2,3)
    - 재귀호출로 인해 winner1 = 학생 2, winner2 = 학생 3로 나눠지고, 가위바위보를 하게됨.
    - 가위바위보 승자가 결승전의 winner2가 됨
'''