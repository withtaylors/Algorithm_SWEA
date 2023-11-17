#테스트 케이스 수 입력받기
T = int(input())

#테스트 케이스 각각 처리하기
for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    #print(nums)
    #[3, 17, 1, 39, 8, 41, 2, 32, 99, 2]

    avg_value = round(sum(nums)/len(nums))
    #print(avg_value)
    #24

    print("#{} {}".format(test_case, avg_value))