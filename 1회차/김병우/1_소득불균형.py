import sys

sys.stdin = open("_소득불균형.txt")
# 평균보다 작은 사람들의 수를 count 하면됨

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    money = map(int, input().split())

    money = list(money)
    # print(money)

    avg_ = sum(money) / N
    # print(sum_)
    
    count = 0

    for i in money:
        if i <= avg_: # 평균값보다 입력된 값이 작으면 +1
            count += 1
    # print(count)

    print(f'#{test_case} {count}')