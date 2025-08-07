import sys
sys.stdin = open('input.txt')

def cul(node):
    if len(tree[node]) == 2:
        return int(tree[node][1])

    op = tree[node][1]
    left = cul(int(tree[node][2]))
    right = cul(int(tree[node][3]))

    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left / right

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [None] * (N + 1)

    for _ in range(N):
        info = input().split()
        idx = int(info[0])
        tree[idx] = info

    print(f"#{test_case} {int(cul(1))}")