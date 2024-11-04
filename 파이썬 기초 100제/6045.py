# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기

# 정수 3개를 입력받아 합과 평균을 출력해보자.

n1, n2 , n3 = map(int, input().split())

sum = n1+n2+n3
avg = (n1+n2+n3)/3

avg = float(avg)

print(sum, format(avg,".2f"))