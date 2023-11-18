#딕셔너리, 문자열 인덱싱을 통해 풀었다.
# month를 키로, month에 해당하는 day의 최대 값 을 value로 한 딕셔너리 days를 만들었다.
# 테스트 케이스 값을 string으로 전환한 후, 문자열 인덱싱을 통해 year,month,day로 나누었다.
# year는 모든 값이 유효하므로 검사하지 않아도 되고, month의 경우 1~12 중 하나인지,
# day는 0 보다 크고 month에 해당하는 값보다 작거나 같은지 검사한다.
# 모든 조건을 만족한다면 '#[test_case] [year]/[month]/[day] '를 출력한다.
# 여기서 주의할 점은 1월의 경우 01 과 같은 방식으로 출력되어야 하기 때문에
# int 로 바꿨다가('01' -> 1) str(1 -> '1') 로 바꾼 후 출력하면 안된다.
# 만약 하나라도 조건을 만족하지 못하면 '#[test_case] -1'을 출력한다.

import sys;
sys.stdin = open('input.txt', 'r')

T = int(input())

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for testcase in range (1, T+1):
    case = str(input())
    year = case[0:4]
    month = case[4:6]
    day = case[6:]

    if (0 < int(month) <13 and 0 < int(day) <= days[int(month)]):
        result = year + "/" + month + "/" + day
    else:
        result = "-1"

    print("{} {}".format(testcase, result))