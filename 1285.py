import sys;
sys.stdin = open('input.txt', 'r')

# 가장 가깝게 돌이 떨어진 위치, 0 사이의 거리차이, 몇 명이 그렇게 돌을 던졌는지 구하기
T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    distance_list = list(map(int, input().split()))

    for i in range(len(distance_list)):
        distance_list[i] = abs(distance_list[i])

    print(f'#{testcase} {min(distance_list)} {distance_list.count(min(distance_list))}')