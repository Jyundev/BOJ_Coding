# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))

    return strings

# 다른 풀이
sorted(strings, key=lambda x: x[n])

# [1차] 비밀지도
# 빈공간 채우기 : zfill, rjust 
def solution(n, arr1, arr2):
    bit_arr = [bin(a1 |a2)[2:].zfill(n) for a1, a2 in zip(arr1, arr2)]
    answer = []
    # answer = ["#" if s == "1" else " " for a in answer for s in a]
    for a in bit_arr:
        result = ""
        for s in a:
            if s == "1":
                result+="#"
            else:
                result+=" "
        answer.append(result)
    
    return answer


# 다른풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer