# 행렬의 덧셈
# 런타입 에러
def solution(arr1, arr2):
    answer = [[],[]]
    for i, (a, b) in enumerate(zip(arr1, arr2)):
        for x, y in zip(a,b):
               answer[i].append(x+y)

    return answer

# 성공
def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]  
    for i, (a, b) in enumerate(zip(arr1, arr2)):
        for x, y in zip(a, b):
            answer[i].append(x + y)  
    return answer


# 다른 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]


# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print("*"*a)
    
# 다른풀이 
answer = ('*'*a +'\n')*b

#최대공약수와 최소공배수
def gcp_func(n, m): # m > n
    mod = m % n
    if mod == 0:
        return n
    return gcp_func(mod, n)

def solution(n, m):
    gcp = gcp_func(min(n, m), max(n, m))
    return[gcp, n*m/gcp]

# 예산
def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        arr = sorted(d)
        answer = len([i for i in range(1, len(arr)+1) if sum(arr[:i]) <= budget ])
    return answer

# 3진법 뒤집기
def solution(n):
    ternary = ''
    answer = 0
    while n > 0:
        ternary = str(n%3)+ ternary
        n = n//3
        
    for idx, v in enumerate(ternary):
        answer += 3**int(idx)*int(v)
    
    return answer


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

# 크기가 작은 부분문자열
def solution(t, p):
    answer = 0
    for i in range(len(t)-(len(p)-1)):
        if int(t[i:i+len(p)]) <= int(p):
            answer+=1
    return answer

# 이상한 문자 만들기
# +6접 받음 히히 
def solution(s):
    answer = []
    s = s.replace(" ", '-')
    for v in s.split('-'):
        answer.append("".join([w.upper() if i % 2 == 0 else w.lower() for i, w in enumerate(v)]))
        
    return " ".join(answer)


# 삼총사