import sys;
sys.stdin = open('input.txt', 'r')

# 두 자연수 입력받기
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
