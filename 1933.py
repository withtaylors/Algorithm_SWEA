import sys;
sys.stdin = open('input.txt', 'r')

# 입력한 정수 받기
N = int(input())

# 약수 구하기 + 오름찬순 정렬
for i in range (1, N+1):
    if(N % i == 0):
        print(i, end=" ")