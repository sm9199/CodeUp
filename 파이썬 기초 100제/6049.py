# 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2

# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.


n1, n2 = map(int, input().split())

if n1==n2:
    print("True")
else:
    print("False")