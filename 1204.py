import sys;
sys.stdin = open('input.txt', 'r')

T = int(input())

# 1. 우리가 알고싶은 최빈수 값(mode) 변수를 만든다.
# 2. 최빈수 딕셔너리(dictionary)를 만든다. ex) 8이 2개, 4가 3개일 경우 {8:2, 4:3}
# 3. 최빈수 딕셔너리를 숫자값(key)과 카운트값(value)을 items()로 꺼내와 for문을 돌린다.
# 4. 카운트값(value)이 최댓값(즉, 최빈수)일때 최빈수값(mode)에 숫자값(key)을 넣는다.
# 5. 꺼낸 카운트값이 최댓값과 같을 경우 숫자값을 비교하여 큰 숫자를 넣는다.
# 6. 최빈수 값(mode)을 출력한다.

for testcase in range(1, T+1):
    test_number = int(input())
    score_list = list(map(int, input().split()))
    mode = 0

    #2
    count_dic = {}
    for i in score_list:  # 입력받은 숫자 리스트를 순회
        if i in count_dic:  # 만약 현재 숫자가 딕셔너리에 이미 키로 존재한다면
            count_dic[i] += 1  # 해당 숫자의 빈도수를 1 증가시킴
        else:
            count_dic[i] = 1  # 만약 딕셔너리에 현재 숫자의 키가 없다면, 새로운 키를 생성하고 빈도수를 1로 설정
            print(count_dic)

    #3
    max_count = 0  # 현재까지의 최댓값을 기록하는 변수
    for key, value in count_dic.items():  # 딕셔너리의 각 아이템을 순회
        if max_count < value:  # 현재까지의 최댓값보다 현재 숫자의 빈도수가 크면
            max_count = value  # 최댓값을 현재 숫자의 빈도수로 업데이트하고
            mode = key  # 최빈수를 현재 숫자로 설정
        elif max_count == value:  # 최댓값과 현재 숫자의 빈도수가 같다면
            if mode < key:  # 현재 최빈수보다 현재 숫자가 더 크면
                mode = key  # 최빈수를 현재 숫자로 업데이트
    # 6
    print('#{} {}'.format(test_number, mode))