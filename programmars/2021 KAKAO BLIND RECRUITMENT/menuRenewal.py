# 메뉴리뉴얼
# 마지막 입출력 예제에서 오류
# ["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
# 왜지...?

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        # print(c)
        temp = []
        for order in orders:
            permute = combinations(order,c)
            # print(list(permute))
            temp += permute
            
        counter_temp = Counter(temp).most_common()
        print(counter_temp)
        answer += [''.join(menu) for menu, cnt in counter_temp if cnt > 1 and cnt == counter_temp[0][1] ]

    return sorted(answer)
            

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))