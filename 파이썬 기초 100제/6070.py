# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

n = int(input())

if n//3==1:
    print("spring")
elif n//3==2:
    print("summer")
elif n//3==3:
    print("fall")
else:
    print("winter")