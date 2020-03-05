def solution(n, lost, reserve):
    reserve,lost = list(set(reserve) - set(lost)), list(set(lost) - set(reserve))
        
    for i in reserve :
        if i-1 in lost :
            lost.pop(lost.index(i-1))
            continue
        if i+1 in lost :
            lost.pop(lost.index(i+1))
            continue
    answer = n - len(lost)   
    return answer

print(solution(	5, [2, 4], [3]))
