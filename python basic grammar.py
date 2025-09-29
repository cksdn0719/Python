# 정수형 및 실수형

a = 3
print(a)
print(type(a))

b = 4.12E3
print(b)
print(type(b))

c = 0o10 # 8진수
print(c)
print(type(c))

d = 0xb # 16진수
print(d)
print(type(d))

# 사칙연산

a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a // b) # 몫을 보여줌
print(a % b) # 나머지를 보여줌

# 문자형

a = "hello"
b = "world"
c = 'input "" in string ' # 문자열 안에 "" 혹은 '' 넣기
d = "input \"\" in string" # ""문자열 안에 \ 이용해서 ""넣기
print(a + " " + b) 
print(type(a))

# 백슬래쉬 활용

# 줄바꿈 \n
print("hello world \nnice to meet you")
print("\n")
a = '''hello world
nice to meet you
'''
print(a)

# 백슬래쉬 표현
print("\\") 

# 큰 따옴표 작은 따옴표 표시
print(" \" \' ")

# 문자열 연산하기

head = "python"
tail = " is fun"
print(head + tail)

a = "hello \t" # \t : tab만큼의 거리를 만들기
print(a*3)

# 문자열 곱하기 응용하기

print("=" * 50)
print("문자열 곱하기 응용하기")
print("=" * 50)

# 문자열 길이 구하기

a = "hello world"
print(len(a)) # 공백 포함

b = "안녕하세요"
print(len(b))

# 문자열 인덱싱과 슬라이싱

a = "my name is chanwoo"

print(a[3],a[5]) # 시작은 m = 0 부터 인덱스 시작
print(a[-1]) # 거꾸로 이동함 o = -1

print(a[0:5]) # 슬라이싱 - 변수명[ : : ] 각각 이상, 미만, 간격 
# ex) a[0:5] - 이상 5미만, ex) a[0 : ] 미만의 자리가 비어있을 경우 끝까지를 의미

print(a[::3])
# 3칸 간격으로 인덱싱함

# 문자열 인덱싱과 슬라이싱 활용

data = "2020 08 19 sunny"
date = data[0:10]
weather = data[10:]

print(date)
print(weather) # date와 weather data 나누기

# 문자열 포매팅

a = "i eat %d apples" %20 
print(a)

b = "today = %s" % "sun" # %s는 어떤 type이여도 수용이 가능함
print(b)

num = 20 # int 변수 만들어서 포매팅 하기
c = "my age = %d" %num 
print(c)

string = "world!" #string 변수 만들어서 포매팅 하기
d = "hello %s" %string
print(d)

date = 20
weather = "rainy"
e = "today is %d and weather is %s" %(date,weather)
print(e)


# 정렬과 공백

blank_1 = "%10s" % "HI" # "HI"를 제외하고 앞에 8칸의 공백이 들어감
print(blank_1) 

blank_2 = "%-10s" % "HI" # "HI"를 제외하고 뒤에 8칸의 공백이 들어감
print(blank_2) 

# 소수점 표현하기

a = "%.4f" % 5.1028801 
print(a) # 4번째 소수점 까지 표현하고 뒤에 소수점은 올림

# 왼쪽 정렬과 오른쪽 정렬

a = "{0:<10}".format("hi")
print(a) # 왼쪽 정렬 "hi"를 제외하고 오른쪽에 8칸의 공백이 들어감
b = "{0:>10}".format("hi")
print(b) # 오른쪽 정렬 "hi"를 제외하고 왼쪽에 8칸의 공백이 들어감
c = "{0:^10}".format("hi")
print(c) # 가운데 정렬 "hi"를 제외하고 양쪽에 각각 4칸의 공백이 들어감

# 가운데 정렬 활용

c = "{0:=^10}".format("hi")
print(c) # 공백 대신 "=" 표시가 들어감 다른 표시도 괜찮음

# 소수점 표현하기 활용
f = 3.141592
a = "{0:0.4f}".format(f)
print(a)

# 최신 포매팅 - F 포매팅
name = '홍길동'
age = 30

a = f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(a)

b = f"나의 이름은 {name+"님"}입니다. 나이는 {age+1}입니다." # 중괄호 속 연산 가능 
print(b)

c = f'{"hi":<10}' # 정렬 기능 
print(c)
c = f'{"hi":>10}'
print(c)
c = f'{"hi":^10}'
print(c)

d = 3.141592 # 소수점 표현
e = f'{d:0.3f}'
print(e)

# 메소드를 활용한 문자열의 여러가지 기능

a = "hobby"
print(a.count('b'))

b = "hobby"
print(b.find('b')) # index를 사용해도 되나 index는 없는 문자를 찾을 시 오류를 발생

c = " and ".join("abcd") # 해당 기능은 list로도 구현 가능
print(c)

d = " and ".join(['a','b','c','d']) # 해당 기능은 list로도 구현 가능
print(d)

# 소문자 대문자 변환

a = "hello world"
print(a.upper())

a = "HELLO WORLD"
print(a.lower())

# 공백 지우기

char = "coding world"
a = " hello"
b = "hello "
c = " hello "

print(char + a)
print(char + a.lstrip())  # 기존에 있던 hello 왼쪽 공백이 사라지면서 world와 hello가 붙음

print(b + char)
print(b.rstrip() + char) # 기존에 있던 hello 오른쪽 공백이 사라지면서 hello와 coding이 붙음

print(char + c + char)
print(char + c.strip() + char) # 기존에 있던 hello 양옆 공백이 사라지면서 전부 붙음

# 문자열 바꾸기

a = "Life is so beatiful"
print(a)
print(a.replace("Life", "My face")) # ctrl F3 으로도 가능


# 문자열 나누기

a = "Life is so beatiful"
print(a)
print(a.split()) # 실행 시 문자열 속 변수들의 리스트를 반환

# List의 개념과 활용

list = [1,2,3,4,5]
print(type(list))

a = [1,2,"list","code"] # 여러가지 자료형을 담을 수 있고 리스트 안에 리스트를 담을 수도 있음

# List의 인덱싱과 슬라이싱

list = [1,2,3,4,5]
print(list[0])

list = [1,2,[1,2,3]] # List 속 List
print(list[2]) 

list = [1,2,[1,2,3]]
print(list[0:3]) 

# List 속 List 인덱싱과 슬라이싱

list = [1,2,['a','b','c']]
print(list[2][1])

list = [1,2,['a','b','c']]
print(list[2][0:3])

# List 연산

a = [1,2,3]
b = [4,5,6]

print(a+b)
print(a*3)

# List 길이 구하기

a = [1,2,3]
print(len(a))

# List 값 변환

a = [1,2,3]
a[2] = 4

print(a)

a = [1,2,3]
del a[1]

print(a)

a = [1,2,3]
del a[0:] # 슬라이싱으로 전부 삭제

print(a)

# List에 요소 추가

a = [1,2,3]
a.append(4) 
a.append([5,6])

print(a)

# List 정렬

a = [10,9,8,7,6,5,4,3,2,1] # 올림차순
a.sort()
print(a)

a.reverse() # 내림차순
print(a)

# List에서 index finding

a = [10,9,8,7,6,5,4,3,2,1]
print(a.index(4))

# List에 요소 삽입

a = [1,2,3]
a.insert(0,2) # append와 좀 다른 점 - 특정 인덱스에 어떤 값을 삽입하는 것은 insert 마지막에 값을 넣는 것은 append

print(a)

# List의 요소 제거

a = [1,2,3,4,1,2,3,4]
a.remove(3) # 가장 처음 나오는 설정된 X의 값을 삭제 시킴 

print(a)

# List 요소 끄집어 내기

a = [1,2,3,4,1,2,3,4]
a.pop() # 가장 뒤에 있는 요소를 끄집어 냄

print(a.pop())
print(a)

# List 요소 개수 세기

a = [1,2,3,4,1,2,3,4]
a.count(1)
print(a.count(1))

