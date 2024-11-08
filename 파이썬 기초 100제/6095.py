# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기


lst = []         # 바둑판 생성

for i in range(20): # 20x20 가로 바둑판 생성
    lst.append([])
    for j in range(20): # 20x20 세로 바둑판 생성
        lst[i].append(0)
        

n = int(input()) # 바둑알 올릴 개수

for i in range(n):
    x,y = map(int,input().split())
    lst[x][y] = 1
    
for i in range(1,20):
    for j in range(1,20):
        print(lst[i][j], end = ' ')
        
    print()