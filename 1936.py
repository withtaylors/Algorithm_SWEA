import sys;
sys.stdin = open('input.txt', 'r')

# 무슨 가위바위보 낼건지 받기 - 빈칸으로 나누기
A, B = list(map(int, input().split()))

# 누가 이겼는지 판별하는 과정 작성
# if (a-b) == -1 or (a-b) == 2:
#     print('B')
# else:
#     print("A")
if (A == 1 and B == 3):
    print("A")
elif (A == 3 and B == 1):
    print("B")
elif (A<B):
    print('B')
elif (A>B):
    print('A')