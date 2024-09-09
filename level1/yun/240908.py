# 약수의 합
def solution(n):
    sum = 0
    for i in range(1, n+1):
        if n%i == 0:
            sum+=i
    return sum
 
 # 짝수와 홀수
def solution(num):
    return "Even" if num&1 == 0 else "Odd"

# 문자열 내 p와 y의 개수
def solution(s):
    s = str.lower(s)
    return s.count('p') == s.count('y')

from collections import Counter
def numPY(s):
    # Counter(s.lower())는 문자열 s의 각 문자들이 몇 번 등장하는지 세어서 c라는 이름의 Counter 객체를 만듭니다.
    c = Counter(s.lower())
    return c['y'] == c['p'] 

# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)


# 자릿수 더하기
def solution(n):
    return sum(list(map(int,str(n))))

# 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(map(int, reversed(str(n))))

def solution(num):
     return [int(i) for i in str(num)[::-1]]
 
#  정수 내림차순으로 배치하기
def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))
    
# 정수 제곱근 판별
# is_integer() : 정수 판별
import math

def solution(n):
    if math.sqrt(n).is_integer():
        return math.pow(math.sqrt(n)+1, 2)
    else:
        return -1
    
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

# 하샤드 수
def solution(n):
    return n % sum(map(int,str(n))) == 0

# 두 정수 사이의 합
def solution(a, b):
    return sum([i for i in range(min(a,b), max(a,b)+1)])

# 나머지가 1이 되는 수 찾기
def solution(num):
    for i in range(2, num):
        if num % i == 1:
            return i
        
# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [i*x for i in range(1, n+1)]

# 서울에서 김서방 찾기
def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'

# 콜라츠 추측
def solution(num):
    print(num)
    
    global cnt  
    
    if cnt > 500:
        return -1
    
    if num == 1:
        return cnt
    
    cnt += 1
    
    if num % 2 == 0:
        num //= 2  
    else:
        num = num * 3 + 1
    
    return solution(num)

global cnt
cnt = 0


# 음양 더하기
def solution(absolutes, signs):
    sum = 0
    for a, s in zip(absolutes, signs):
        if s:
            sum+=a
        else:
            sum-=a
    return sum

# 없는 숫자 더하기
def solution(numbers):
    return sum(set(range(10)) - set(numbers))


# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    result = sorted([i for i in arr if i % divisor == 0])
    if len(result) == 0:
        return [-1]
    return result

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_idx = arr.index(min(arr))
    arr.pop(min_idx)
    return arr


def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_v = min(arr)
    arr.remove(min_v)
    return arr

# 핸드폰 번호 가리기
def solution(phone_number):
    return len(phone_number[:-4])*'*'+phone_number[-4:]