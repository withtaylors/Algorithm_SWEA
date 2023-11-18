import sys;
sys.stdin = open('input.txt', 'r')

T = int(input())

for testcase in range(1,T+1):
    a, b = map(int, input().split())
    if(a > b):
        result = ">"
    elif(a == b):
        result = "="
    elif (a < b):
        result = "<"

    print('{} {}'.format(testcase, result))