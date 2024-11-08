# 6086 : [기초-종합] 거기까지! 이제 그만~

num = int(input())
n = 0
sum = 0

while True:
    sum += n
    n += 1
    if sum>= num:
        break
    
    
print(sum)