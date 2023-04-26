print("hello world")

#문자열 indexing
a="Life is too short, You need python"
print(a)
print(a[0], a[3], a[12], a[-3])
print(a[:4], a[5:7], a[12:17])
print(a[:11], a[11:])
print(a[:])

#슬라이싱으로 문자열 나누기
a="20230427happy"
date = a[:8]
weather = a[8:]
print (date)
print(weather)

#pithon이라는 문자열을 python으로 바꾸려면?
a= "pithon"
print (a[:1]+"y"+a[2:])

#문자열 포매팅(Formatting) : 문자열 안에 특정값만 바꿔야 할때 사용
#숫자 넣기
a = "I eat %d apples." %3 #%d는 문자열 포맷코드 : 숫자넣을 때 사용
print(a)
#문자열 넣기
a = "I eat %s apples." %"five" #%s는 문자열을 넣을때 사용
print(a)
#변수 넣기
number =3
a = "I eat %d apples." %number
print(a)
#2개 이상의 값 넣기
number=10
day = "three"
a="I ate %d apples. so I was sick for %s days." %(number, day)
print(a)
#%를 문자열에 쓰는경우
a= "Error is %d%%."%98
print(a)
#page60