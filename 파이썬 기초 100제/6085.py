# 6085 : [기초-종합] 그림 파일 저장용량 계산하기

r,g,b = map(int, input().split())

mb = (r*g*b) / 1024 / 1024 / 8
print('%.2f MB' %mb)