# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기

# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.

num = int(input())

if num <0:
    if num %2==0:
        print("A")
    else:
        print("B")
        
elif num>0:
    if num%2==0:
        print("C")
    else:
        print("D")
        
        