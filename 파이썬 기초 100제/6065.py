# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기

# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

n1, n2, n3 = map(int,input().split())

if n1 % 2 == 0:
    print(n1)
if n2 % 2 == 0:
    print(n2)
if n3 % 2 ==0 :
    print(n3)