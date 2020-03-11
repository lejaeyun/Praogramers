def solution(heights):
    answer = []
    length = len(heights)
    for i in range(length-1,-1,-1) :
        for j in range(i-1, -1, -1) :
            if heights[i] < heights[j] :
                answer.append(j+1)
                break
            else :
                if j == 0 :
                    answer.append(0)
    answer.append(0)
    answer.reverse()
    return answer
