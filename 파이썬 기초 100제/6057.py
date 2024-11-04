# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기

# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.


n1,n2 = map(int, input().split())

print((not bool(n2) and not bool(n1)) or (bool(n1) and bool(n2)))