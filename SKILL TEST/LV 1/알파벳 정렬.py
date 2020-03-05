def solution(s):
    answer = ''
    li = list()
    for ss in s :
        li.append([ord(ss),ss])    
    li.sort(reverse = True)
    for ss in li :
        answer += ss[1]
    return answer
