def solution(participant, completion):
    participant.sort()
    completion.sort()
    i = 0
    index = len(participant)
    while i < index - 1:
        if participant[i] != completion[i] :
            return participant[i]
        i = i + 1
    return participant[i]
