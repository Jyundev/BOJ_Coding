# 시저 암호
def solution(s, n):
    answer = ''
    for w in s:
        if w == " ":
            answer+= " "
        elif ord(w) in range(97, 123): 
            if (ord(w)+n) > 122:
                answer+=chr(ord(w)-26+n)
            else:
                answer+=chr(ord(w)+n)
        else:
            if (ord(w)+n) > 90:
                answer+=chr(ord(w)-26+n)
            else:
                answer+=chr(ord(w)+n)
                
    return answer


# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# 가장 가까운 같은 글
def solution(s):
    answer = []
    d = dict()
    for i, w in enumerate(s):
        if w in list(d.keys()):
            answer.append(i-d[w])
            d[w] = i     
        else:
            d[w] = i
            answer.append(-1)
        
    return answer

# 숫자 문자열과 영단어
def solution(s):
    num = range(0, 10)
    eng = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    d = dict(zip(eng, num))
    
    for e in eng:
        if s.__contains__(e):
            s = s.replace(e, str(d[e]))
            

    return int(s)

# 다른 풀이

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)