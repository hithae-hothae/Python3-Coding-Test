import copy
import collections

def solution(participant, completion):
    answer = []
    par2 = copy.deepcopy(participant)
    comp2 = copy.deepcopy(completion)
    for p in participant :
        for c in completion :
            if p == c : 
                del par2[par2.index(p)]
                del comp2[comp2.index(c)] 
    answer = par2
    return answer


def solution2(participant, completion):
    answer = copy.deepcopy(participant)  
    
    for person in completion:
        del answer[answer.index(person)]
    
    return answer[0]


def solution3(participant, completion):
    
    answer = collections.Counter(participant) - collections.Counter(completion)

    return answer.keys()


print (solution3(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))