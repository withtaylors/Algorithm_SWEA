import sys;
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 개수
T = int(input())

for testcase in range(1, T+1):
    a, b = map(int, input().split())
    value = a//b
    rest = a % b
    print(f'#{testcase} {value} {rest}'.format())
    #print("#{} {} {}".format(testcase, a//b, a%b))