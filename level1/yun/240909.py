# 가운데 글자 가져오기
def solution(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
    
# 수박수박수박수박수박수?
def solution(n):
    arr = ['수', '박']    
    if(n%2==0):
        return ''.join(arr * (n//2))
    else:
        return ''.join(arr * (n//2))+'수'
        
def solution(n):
    # 함수를 완성하세요.
    str = "수박"*n
    return str[:n]

# 내적
def solution(a, b):
    answer = 0
    for x, y in zip(a,b):
        answer += x*y 
    return answer

# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if (i ** 0.5).is_integer():
            answer -= i
        else:
            answer += i
            
    return answer

# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer

# 부족한 금액 계산하기
def solution(price, money, count):
    p = sum([c*price for c in range(1, count+1)])
    if p - money <= 0:
        return 0
    else:
        return p - money
        

# 문자열 다루기 기본
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if ord(i) >= 65:
            return False
    
    return True
        
def alpha_string46(s):
    #함수를 완성하세요
    return s.isdigit() and len(s) in [4,6]

