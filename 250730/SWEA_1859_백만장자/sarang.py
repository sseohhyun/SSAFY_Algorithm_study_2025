t = int(input())
for case in range(t):
    cost_list = list(map(int, input().strip().split()))
    
    cost_max = max(cost_list)
    count = 0
    total = 0

    if (cost_list.index(cost_max) == 0) and (cost_list.count(cost_max) == 1):
        print(f'#{case + 1} {total}')
    else:
        for i in range(cost_list.index(cost_max)):
            total -= cost_list[i]
            count += 1
        total = total + (count * cost_max)
        
    print(total)



