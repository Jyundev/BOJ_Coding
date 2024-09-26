# 콜라 문제
def solution(a, b, n):
    answer = 0
    while (n >= a ):
        answer +=n // a * b
        n = n % a + (n // a * b)
    return answer


# 명예의 전당 (1)
def solution(k, score):
    answer = []
    
    for i in range(len(score)):
        if i >= k:
            answer.append(sorted(score[:i+1], reverse = True)[k-1])
        else:
            answer.append(min(sorted(score[:i+1])))
                
    return answer

# 다른풀이
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer


import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer

# 추억 점수
def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    answer = []
    for p in photo:
        score = 0
        for friend in p:
            if friend in score_dict.keys():
                score += score_dict[friend]
        
        answer.append(score)
            
    return answer

# 카드 뭉치
