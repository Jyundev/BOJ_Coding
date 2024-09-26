# 삼총사
def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                arr = []
                arr.extend([number[i],number[j], number[k]])
                if sum(arr) == 0:
                    answer += 1
    return answer

#다른 풀이 
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

# 최소직사각형
def solution(sizes):
    answer = 0
    small = []
    big = []
    for (w, h) in sizes:
        small.append(min(w,h))
        big.append(max(w,h))
    
    answer = max(small) * max(big)
 
    return answer

# 다른풀이
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)

