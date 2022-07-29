import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for test_case in range(0, T + 1):
    n = int(input())

    score = map(int, input().split())
    # print(score) # 안나오는데?, 출력은 되는데 주소값 나오는 듯?

    list_ = [0] * 1000 # 리스트 0 값을 1000개 만들어 줌
    # print(list_)

    for i in score:
        # print(i) # 점수들 출력됨, int
        # print(list_[i]) # 0000...만듬
        list_[i] += 1 # score에 해당하는 숫자가 들어올때마다 1을 더하고 같은게 있으면 더한 숫자에 1을 더한다
        # print(list_[i]) # 그리고 그 중 가장 숫자가 큰 것을 골라 출력하면 되지 않을까?
    # print(list_) # 리스트에 중복포함해서 만들어짐 같은 숫자가 겹쳐서 나오니까 뒤로 갈수록 숫자가 커짐
    h_score = max(list_) # list에서 가장 큰 값을 h_score에 저장함
    # print(h_score) # 가장 큰 수

    answer = [] # 정답이 될 리스트 하나 만듬
    # print(len(list_)) # 1000
    for j in range(len(list_)): # 1000 순회, 리스트의 개수만큼 순회
        if list_[j] == h_score: 
            answer.append(j) # 제일 큰 값들을 answer 저장


    print(f'#{n} {max(answer)}') # max사용해서 answer 중 가장 큰 값 저장