import sys;
sys.stdin = open('input.txt', 'r')

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

result = nums[N//2]
print(result)