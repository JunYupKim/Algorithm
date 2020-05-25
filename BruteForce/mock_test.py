# Programmers 
# Brute Force
# 모의고사 
def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [ 2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        if answers[i] == supo1[i%5]:
            cnt1 += 1
        if answers[i] == supo2[i%8]:
            cnt2 += 1
        if answers[i] == supo3[i%10]:
            cnt3 += 1
        
    max_ = max(cnt1,cnt2,cnt3)
    
    if cnt1 == max_:
        answer.append(1)
    if cnt2 == max_:
        answer.append(2)
    if cnt3 == max_:
        answer.append(3)
        
    return answer