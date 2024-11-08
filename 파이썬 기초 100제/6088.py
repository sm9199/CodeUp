# 6088 : [기초-종합] 수 나열하기

a,d,n = map(int, input().split())

for i in range(0,n):
    if i == n:
        break
    
print(a+d*i)