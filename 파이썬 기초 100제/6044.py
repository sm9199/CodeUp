# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

n1, n2 = map(int, input().split())

div = n1/n2

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)
print(n1%n2)
print(format(div,".2f"))