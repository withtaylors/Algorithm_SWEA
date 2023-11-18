import sys;
sys.stdin = open('input.txt', 'r')

# 숫자 입력 받기
N = int(input())

# 1부터 주어진 숫자 모두 더하기
result = 0
for i in range (1, N+1):
    result += i
print(result)