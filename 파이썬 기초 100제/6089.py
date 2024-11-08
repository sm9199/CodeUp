# 6089 : [기초-종합] 수 나열하기2

a,r,n = map(int, input().split())

for i in range(0,n):
    if i == n:
        break
    
print(a*r**i)