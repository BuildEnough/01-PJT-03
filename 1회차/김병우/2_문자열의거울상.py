import sys
sys.stdin = open("_문자열의거울상.txt")


T = int(input())
for test_case in range(1, T + 1):
    word = input()
    
    word = list(word)
    # print(word)
    
    re_word = word[::-1]
    # print(re_word)
    # ['q', 'p', 'p', 'd', 'b']
    # ['d', 'b', 'b', 'p', 'p', 'p', 'q', 'q', 'q', 'q']
    
    
    dict_ = {
        'q': 'p',
        'p': 'q',
        'b': 'd',
        'd': 'b'
    }

    for i in range(len(re_word)):
        re_word[i] = dict_[re_word[i]]
    # print(re_word)
    # ['p', 'q', 'q', 'b', 'd']
    # ['b', 'd', 'd', 'q', 'q', 'q', 'p', 'p', 'p', 'p']

    answer = ""

    for j in re_word:
        answer += j + ""
    # print(answer)    

    print(f'#{test_case} {answer}')

        

