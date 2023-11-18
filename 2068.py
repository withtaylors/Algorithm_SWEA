import sys;

sys.stdin = open('input.txt', 'r')

T = int(input())

for testcase in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    result = max(nums)
    # result = nums[9]
    print('{} {}'.format(testcase, result))