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

# 튜플 - List와 달리 변형이 불가능하다 ex) sort, insert,remove,pop,del 등등

a1 = ()
print(type(a1))

a2 = (1, ) # 하나의 값을 넣을 땐 무조건 ","를 넣어야 한다
print(a2[0])

a3 = 1,2,3
print(type(a3)) # 괄호를 없이 해도 튜플로 나온다

# 튜플 요소 제거

a1 = 1,2,3,'a','b'
# del a1[0] # 튜플은 변경이 불가능 함

# 튜플은 리스트와 거의 동일함 인덱싱과 슬라이싱 전부 가능

# 튜플의 연산

a1 = 1,2,3
a2 = 4,5

a3 = a1 + a2

print(a3)

a1 = 1,2,3
a2 = a1 *2

print(a2)

# 튜플 길이 구하기

a1 = 1,2,3
print(len(a1))

# Dictionary 

dic1 = {'name':'yuk', 'phone' : '010-1234-1234'}
print(type(dic1))
print(dic1)

dic2 = {'a': [1,2,3]}
print(dic2)

# Dictionary의 특성들

a = {1 : 'a'}
a[2] = 'b' # Dic에 새로운 key와 value 추가 [] 안쪽이 key, 값이 value
print(a)

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
del a['name'] # del로 삭제할 땐 [] 안에 key 넣어주기
print(a)

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
print(a[1]) # key를 넣으면 value를 준다


a = {1 :"HI", 1: "BYE"}
print(a) # key가 중복되면 뒤에 있는 key가 활성화 된다. 즉 덮어씌워지는 것이다

# Dictionary 관련 함수

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
print(a.keys()) # keys 함수는 해당 Dic에 key 값들만 선택해 List로 반환한다

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
print(a.values()) # values 함수는 해당 Dic에 value 값들만 선택해 List로 반환한다

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
print(a.items()) # items 함수는 해당 Dic에 key,value 값 모두 선택해 List로 반환한다

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
a.clear() # 값을 싹 날리는 함수다 따라서 빈 Dic을 반환한다
print(a)

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
print(a.get(1)) # key를 통해 value를 얻는 함수
print(a.get('age','값이 존재하지 않음')) # Dic에 없는 key를 넣었을 때 default로 NONE을 반환함. 하지만 옆에 ','를 쓰고 message를 남길 경우 message를 반환함.

a = {1: 'a', 2: 'b', 'name': 'yuk', 3:  [1,2,3]}
print('name' in a) # True, False 둘 중의 하나의 값을 반환함

# 집합 자료형

a1 = set([1,2,3])
print(a1) # set은 순서가 정해진 것이 아니기 때문에 indexing을 할 수 없음
print(type(a1))


a1 = set('Hello')
print(a1) # set은 중복된 것을 허용하지 않는다 따라서 ll이 두번 들어갔지만 반환은 l 한개만 한다
print(type(a1))

a1 = set([1,2,3])
li =list(a1) # indexing을 하려면 데이터 변환을 통해 List로 만들어서 indexing 해야함
print(li[0])

a1 = set([1,2,3])
tu = tuple(a1) # tuple도 동일함
print(tu[0])

# 교집합, 합집합, 차집합 구하기

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(s1&s2) # 교집합
print(s1.intersection(s2)) # 교집합 - intersection이란 함수를 이용함

print(s1|s2) # 합집합
print(s1.union(s2)) # 합집합 - union이란 함수를 이용함

print(s1-s2) # 차집합
print(s1.difference(s2)) #차집합  - difference란 함수를 이용함

s1 = set([1,2,3,4,5])
s1.add(6) # set의 끝에 값 1개를 추가함
print(s1)

s1 = set([1,2,3,4,5])
s1.update([6,7,8]) # set의 끝에 값 여러개를 추가함
print(s1)

s1 = set([1,2,3,4,5])
s1.remove(2) # set의 특정 값을 제거함
print(s1)

# set은 언제 활용할까

li = [1,2,2,2,2,3,3,3,4,4,5,5,6] # List에 중복된 요소가 있을 경우
s1 = set(li) # 집합의 특성인 중복 제거를 이용한다
print(s1)  
print(type(s1)) # type이 set이다

li_2 = list(s1) # type이 set인 s1을 다시 List로 만들어준다
print(li_2)
print(type(li_2)) # type이 List 이다

# Bool 자료형

a = True # or False
print(type(a))

# 변수

a = [1,2,3]
print(id(a)) # 주소값 표현


a = [1,2,3]
b = a # List 복사 시 주소값은 동일 즉 a = b임
print(id(a)) 
print(id(b)) 

print(a is b) # bool을 활용해 둘의 주소값이 같은지 직관적으로 확인 가능

# 변수의 복사

a = [1,2,3]
b = a 
a[0] = 4

print(a)
print(b) # b는 a와 동일하기 때문에 a 변경 시 b도 바뀐다


a = [1,2,3]
b = a[:] # a list를 슬라이싱 해서 새로운 list를 b에 넣어서 저장했으니 a와 b는 주소값이 동일하지 않음
a[0] = 4 # a의 요소를 indexing하여 값을 변경해도 b는 독립된 공간임으로 a의 변경 사항이 저장되지 않음

print(a)
print(b)

a = [1,2,3]
b = a[0] # slicing이 아닌 indexing도 마찬가지임
a[2] = 10

print(a)
print(b)

from copy import copy
a = [1,2,3]
b = copy(a) # a의 값들을 단순히 복사해서 새로운 독립된 공간을 만들어 저장시킴 

a = [1,2,3]
b = a.copy() # copy module을 import 해서 사용하는 것이 아닌 copy라는 method를 이용한 복사 방법

print(a is b) # 단순 복사이기 때문에 False가 나옴
print(id(a)) 
print(id(b)) # 따라서 a와 b는 동일하지 않으니 주소값이 다르다

# 변수 생성 방법

a,b = (10,20) # 굳이 따로따로 만들 필요 없다

print(a)
print(b)

a = b = 'python' # 굳이 따로따로 만들 필요 없다

a = 3
b = 5
a,b = b,a # 두 변수의 값을 서로 바꾸는 코드

print(a)
print(b)