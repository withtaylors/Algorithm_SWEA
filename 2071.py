T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    s = sum([x for x in nums if x % 2 == 1])
    print(f'#{test_case} {s}')
