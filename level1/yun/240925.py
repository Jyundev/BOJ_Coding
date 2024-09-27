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
def solution(cards1, cards2, goal):
    idx1 = -1
    idx2 = -1
    for g in goal:
        if g in cards1:
            if idx1 > cards1.index(g):
                return "No"
            else:
                idx1 = cards1.index(g) 
                cards1.remove(g)
                if idx1==len(cards1) and len(cards1)>0:
                    return "No"
                
        else:
            if idx2 > cards2.index(g):
                return "No"
            else: 
                idx2 = cards2.index(g)   
                cards2.remove(g)
                if idx2==len(cards2) and len(cards2)>0:
                    return "No"
            
    return "Yes"


# 다른 풀이 
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

# 폰켓몬
def solution(nums):
    type = set(nums)
    if len(type)>=len(nums) // 2:
        return len(nums) // 2
    else:
        return len(type)



def solution(ls):
    return min(len(ls)/2, len(set(ls)))


# 2016년

def solution(a, b):
    weeks = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    answer = weeks[(sum(days[:a-1])+b+4)%7]
    
    return answer

# 다른 풀이 

import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


# 기사단원의 무기

