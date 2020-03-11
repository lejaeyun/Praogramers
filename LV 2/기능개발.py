def solution(progresses, speeds):
    Check = [False for i in range(len(speeds))]
    answer = []
    b = False
    while True :
        Sum = 0
        for i in range(len(speeds)) :
            progresses[i] += speeds[i]
            if progresses[i] >= 100 :
                Check[i] = True

        for i in range(sum(answer),len(Check)):
            if Check[i] == False :
                break
            else :
                Sum += 1
            if i + 1 == len(Check) :
                b = True

        if Sum != 0 :
            answer.append(Sum)
        if b == True :
            break
    return answer
