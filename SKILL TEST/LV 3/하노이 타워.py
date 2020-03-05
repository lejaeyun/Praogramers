def solution(n):
    answer = hanoi(1,3,2,n)
    return answer
answer = list()
def hanoi(s,e,d,n) :
    global answer
    if n <= 1 :
        answer.append([s,e])
    else :
        hanoi(s,d,e,n-1)
        answer.append([s,e])
        hanoi(d,e,s,n-1)
    return answer
