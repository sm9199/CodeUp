# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기

# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.


w = input()

if w=="A":
    print("best!!!")
elif w=="B":
    print("good!!")
elif w=="C":
    print("run!")
elif w=="D":
    print("slowly~")
else:
    print("what?")