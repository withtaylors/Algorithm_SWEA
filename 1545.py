# 입력받을 숫자
N = int(input())

# 숫자를 거꾸로 0까지 출력
for i in range(N, -1, -1):
    if(N == 0):
        print(0)
    else:
        print(i, end=' ')