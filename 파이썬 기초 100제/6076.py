# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.


n = int(input())

for i in range(0,n+1):
    print(i)