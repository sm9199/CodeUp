﻿# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)

# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

a = ord(input()) # ord는 유니코드 문자 입력 받아서 아스키코드 숫자로 변환
b = a + 1 # 아스키 코드 숫자 + 1을 해줌
c = chr(b) # chr은 숫자 -> 문자형

print(c)
