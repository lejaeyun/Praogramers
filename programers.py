def solution(n, s):
    answer = []
    if s // n == 0 :
        return [-1]
    else :
        answer = [s//n]* n
        for i in range(s - s//n * n) :
            answer[i] += 1
    answer.sort()
            
    return answer

