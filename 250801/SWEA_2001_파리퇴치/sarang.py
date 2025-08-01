import sys
sys.stdin = open('input.txt')
# open 사용해서 input 파일 연다

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().strip().split())
    n_list = []

    # 똥파리 배치
    for _ in range(n):
        n_list.append(list(map(int, input().strip().split())))

    location = []
    def die_location(i, j):
        result = 0
        if (i + m - 1 <= n - 1) and (j + m - 1 <= n - 1):
            for ii in range(i, i+m):
                for jj in range(j, j+m):
                    result += n_list[ii][jj]
        return result

    # 죽일 수 있는 똥파리 수 넣을 리스트
    die = []

    # 완전탐색?
    for i in range(n):
        for j in range(n):
            die.append(die_location(i, j))

    max_die = max(die)
    print(f'#{test_case} {max_die}')
