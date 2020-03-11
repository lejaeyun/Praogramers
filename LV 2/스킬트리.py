def solution(skill, skill_trees):
    answer = 0
    skill_dic = dict()
    for s in skill :
        skill_dic[s] = "False"

    for nowskill in skill_trees :
        answer = answer + 1
        for s in nowskill :
            skill_li = list(skill_dic.keys())
            if s in skill_li :
                index = skill_li.index(s)
                if index == 0 :
                    skill_dic[s] = "True"
                else :
                    if skill_dic[skill_li[index-1]] == "True" :
                        skill_dic[s] = "True"
                    else :
                        answer = answer - 1
                        break
                
            
        for s in skill_dic.keys() :
            skill_dic[s] = "False"
    return answer


