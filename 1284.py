import sys;
sys.stdin = open('input.txt', 'r')

T = int(input())

for testcase in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    if (w > r):
        b = q + (w-r)*s
    else:
        b = q

    if(a>=b):
        cheaperprice = b
    else:
        cheaperprice = a

    print(f'#{testcase} {cheaperprice}')
