import sys
from collections import deque

sys.stdin = open('sample_input.txt')

# key가 value를 이김
play = {
    1: 3,  # 가위(1)는 보(3)를 이김
    2: 1,  # 바위(2)는 가위(1)를 이김
    3: 2   # 보(3)는 바위(2)를 이김
}

def rsp(p1, p2):
    # p1이 이기는 경우
    if play[p1[1]] == p2[1]:
        return p1
    # p2가 이기는 경우
    elif play[p2[1]] == p1[1]:
        return p2
    # 비기는 경우 (번호가 작은 학생이 승리)
    else:
        if p1[0] < p2[0]:
            return p1
        else:
            return p2

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    # 큐에 학생 정보를 (번호, 카드) 튜플 형태로 저장
    students_queue = deque()
    for idx, value in enumerate(cards):
        students_queue.append((idx + 1, value))

    # 큐에 학생이 한 명만 남을 때까지 반복
    while len(students_queue) > 1:
        p1 = students_queue.popleft()  # 큐의 맨 앞에서 학생 1을 꺼냄
        p2 = students_queue.popleft()  # 큐의 맨 앞에서 학생 2를 꺼냄

        winner = rsp(p1, p2)

        students_queue.append(winner)  # 승자를 큐의 맨 뒤에 다시 넣음

    # 큐에 남은 한 명이 최종 우승자
    final_winner = students_queue.popleft()

    print(f'#{test_case} {final_winner[0]}')