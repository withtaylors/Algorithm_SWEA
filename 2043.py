import sys;
sys.stdin = open('input.txt', 'r')

P, K = map(int, input().split())

#1
# python 절댓값 함수 : abs
print(abs(P - K) + 1)


#2
# if (P >= K):
#     print(P-K+1)
# elif (P < K):
#     print(K-P+1+999)

#3
# count = 0
# for i in range(K, P+1):
#    count += 1
#    if i == P:
#        print(count)
#        break