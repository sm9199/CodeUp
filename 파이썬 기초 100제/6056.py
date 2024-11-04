# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

n1,n2 = map(int, input().split())

print((not bool(n2) and bool(n1)) or (not bool(n1) and bool(n2)))