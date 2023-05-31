print("hello world")

print("hello", "world", sep=) ## helloworld

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

##문자열 포매팅(Formatting) : 문자열 안에 특정값만 바꿔야 할때 사용
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

##문자열 관련 함수---------------------------------------------------------------
#문자 개수 반환(len())
#문자 개수 세기(count())
a="hobby"
print(a.count('b'))

#위치 알려주기 1(find(), rfind())
a = "Python is the best choice"
print(a.find('b')) #0부터 세기때문에 b의 위치는 15가 아닌 14이다.
print(a.rfind('k')) #존재하지않는다면 -1을 반환한다.

#위치 알려주기 2(index)
a = "Python is the best choice"
print(a.index('t')) #8
#print(a.index('k')) #존재하지않으면 오류를 발생시킨다. find와의 차이점

#문자열 삽입(join)
",".join('abcd')
",".join(['a','b','c','d'])

#소문자를 대문자로 바꾸기(upper)
a="hi"
a.upper() #HI

#대문자를 소문자로 바꾸기(lower)
a="HI"
a.lower() #hi

#대소문자 한번에 바꾸기swapcase(()
a="HIow"
a.swapcase() #hiOW

#공백 지우기(strip())
str = " hello "
print(str.strip()) #hello

#왼쪽 공백 지우기(lstrip)
a=" hi "
a.lstrip() #'hi '

#오른쪽 공백 지우기(rstrip)
a=" hi "
a.rstrip() #' hi'

#문자열 바꾸기(replace)
a= "Life is too short"
a.replace("Life", "Your leg") #'Your leg is too short'

#문자열 나누기(split)***
a="Life is too short"
a.split() #공백(스페이스바, 엔터)을 기준으로 문자열 나눔
pront(a.split())
b= "a:b:c:d"
b.split(':') #:기호를 기준으로 문자열 나눔
