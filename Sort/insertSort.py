# 삽입 정렬 알고리즘

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            # 두개의 위치를 바꾼다
            array[j], array[j-1] = array[j-1] , array[j] 
        else : 
            break

print("최종 배열 : " , array)
