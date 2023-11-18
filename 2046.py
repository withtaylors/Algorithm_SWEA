import sys;

sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(0, T):
    print("#"*i, end='')