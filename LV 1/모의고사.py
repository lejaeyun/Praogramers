def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    col1 = 0
    col2 = 0
    col3 = 0
    for i in range(len(answers)) :
        if answers[i] == num1[i%5] :
            col1 += 1
        if answers[i] == num2[i%8] :
            col2 += 1
        if answers[i] == num3[i%10] :
            col3 += 1
    m = max(col1,col2,col3)
    if m == col1 : answer.append(1)
    if m == col2 : answer.append(2)
    if m == col3 : answer.append(3)
            
    return answer

