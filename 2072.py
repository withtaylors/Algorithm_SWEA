#테스트 케이스의 개수 입력받는 변수 T
T = int(input())

#여러개의 테스트 케이스가 주어지므로, 각각을 처리
for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    s = sum([x for x in nums if x % 2 == 1])
    print(f'#{test_case} {s}')