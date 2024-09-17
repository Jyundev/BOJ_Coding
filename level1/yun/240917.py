# K번째수
def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1: j])[k-1])
    return answer

# 두 개 뽑아서 더하기

# 다른풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i]+numbers[j]) not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
                
    return answer

# 조합
from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer


# 푸드 파이트 대회
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] <2:
            continue
        answer+=str(i) * (food[i]//2)
    answer = answer + '0' + answer[::-1]
    return answer

# 문자열 내 마음대로 정렬하기
