"""
내장함수: 외부 모듈과 달리 import가 필요하지 않기 때문에 설정없이 바로 사용 가능
"""

# 절대값 함수
print(abs(-3))
print(abs(-3.3))

# all(): 반복 가능한 자료형을 입력 인수로 받으며 x요소가 모두 참일경우 True
print(all([1,2,3]))
print(all([1,2,3, 0])) # 0은 boolean타입으로 형변환시 false
print(all([])) # 입력 인수가 빈 값인 경우는 True

# any(): 반복 가능한 자료형을 입력 인수로 받으며 x요소중 단 하나라도 True일 경우 true
print(any([0,0,0,1])) # 1이 True
print(any([0,0,0])) # 1이 True
print(any([]))

# chr(): unicode를 입력받아 그 코드에 해당하는 문자를 출력하는 함수
print(chr(97)) # unicode는 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 하는 산업 표준

# ord(char): 문자의 유니코드 값을 돌려주는 함수
print(ord("A"))
print(ord("a"))

# dir(): 객체가 자체적으로 가지고 있는 변수나 함수를 출력
print(dir([1,2,3])) # list 자료형의 변수랑 함수를 출력
print(dir({1:'ㅁ'})) # dictionary 자료형의 변수랑 함수를 출력

# divmod(a,b): a를 b로 나눈 몫과 나머지를 튜플형태로 반환
print(divmod(20, 9)) # 튜플반환값은 (a,b)이며 a는 a//b로 구해진 값
                    #                   b는 a%b로 구해진 값

# enumerate(): 순서가 있는 (sequential) 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스값을 포함하는 값을 반환
# 객체가 현재 어느 위치에 있는지 알고 싶을때 유용한 함수
for index, name in enumerate(['apple', 'banana', 'mango']):
    print(index, name)

# eval(expression): 실행 가능한 문자열을 입력받아 문자열을 실행한 결과값을 반환하는 함수
# 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용
print(eval('1+2'))
print(eval(" 'hi' + 'python' "))
print(eval('divmod(4, 3)'))

# filter(a, b)
#       - a는 호출할 함수 이름, b는 함수에 인자값으로 차례대로 들어갈 iterable(반복가능한)  자료형
#       - b인수는 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환값이 '참'인 것만 묶어서 반환
def positive(number):
    return number > 0 # 양수만 filter해서 반환
# filter는 filter객체로 반환되기에 list로 변환 필요
print(list(filter(positive,  [-1, -3, -2, 22, 1.523, 999])))

# lambda로도 구현가능: 일회성 사용 목적으로 함수 생성은 메모리 낭비 유발
# lambda [매개변수] : [수행문]
print(list(filter(lambda x : x > 0, [-1, -3, -2, 22, 1.523, 999])))

# hex(): 정수값을 입력받아 16진수(hexadeciaml)로 변환
print(hex(234))

# id(object): 객체를 입력받아 객체 고유 주소 값(레퍼런스)를 반환
a = 3
b = a
print(id(a))
print(id(b))

# input([prompt]): 사용자 입력을 받는 함수. 문자열을 입력하면 해당 값이 프롬프트가 된다
# print(input("숫자를 입력하세요: "))

# int(x): 문자열 형태의 숫자 혹은 float 형 숫자를 정수 형태로 반환
print(int(2.22))
print(int("2"))

# isinstance(object, class): object인수값이 class의 인스턴스인지 판단하여 true/false 반환
class Person:pass
a = Person()
print(isinstance(a, Person))

# len(s): s의 길이(요소의 전체 개수)를 반환
print(len([1, 2, 3]))
print(len((1, 2, 3)))
print(len({1:'a', 2:'b', 3:'c'}))

# list(s): iterable(반복가능한) 자료형을 입력받아 list로 형변환 한다
print(list({1:'a', 2:'b', 3:'c'}))

# map(function, iterable): 입력받은 자료형의 각 요소를 함수 function이  수행한 결과를 묶어 반환
def two_times(x):
    return x*2
# map함수는 map객체를 반환하기 때문에 리스트로 형변환 필요
# 결국, iterable데이터의 각 요소를 function함수 인자값으로 넘겨 수행값을 묶어 반환하는 함수이다.
print(list(map(two_times, [1, 2, 3, 4])))
# 람다식
print(list(map(lambda x : x*2, [1, 2, 3, 4])))

# max(iterable): 반복 가눙한 자료형을 입력받아 최댓값 반환
print(max([1,2,3]))
print(max("abcdefg")) # 문자열도 반복가능한(iterable)자료형 이다

# oct(): 정수 형태의 숫자르 8진수 문자열로 변환
print(oct(2))

# pow(x,y): x의 y제곱한 결과값 반환
print(pow(2, 4)) # 2^4 or 2**4 or 2x2x2x2

# range(start, stop, step): 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환

# round(number, ndigits): 숫자를 입력받아 반올림해주는 함수
print(round(4.6))
print(round(5.21351, 3)) # 소수점 3번째 자리까지만 반올림

# sorted(iterable): 입력값을 정렬(오름차순)한 후 결과를 '리스트'로 반환
print(sorted([6, 4, 66, 5, 4, 2]))
print(sorted("woifehweifh")) # 문자열도 반복가능한(iterable) 자료형이다
print(sorted((6, 4,1,5,5,6))) # 튜플형을 정렬 후 리스트로 변환

# str(object): 문자열 형태로 객체를 변환하여 반환
print(str(3))
print(str('hihi'))

# sum(iterable): 반복가능한(iterable) 자료형을 입력받아 모든 요소의 합을 반환
print(sum([1,2,3]))
print(sum((23,4,5)))

# zip(*iterable): 동일한 개수로 이루어진 자료형을 묶어주는 역할
#                 *iterable은 반복가능(iterable)한 자료형 '여러 개' 입력 가능을 의미
print(list(zip(['a', 'b', 'c'], [1,2,3], [1.1, 2.2, 3.3])))

# reduce(function, iterable): 반복가능한(iterable) 자료형 내 각 요소를 연산 뒤 이전 연산 결과들과 누적해서 반환해주는 함수
# reduce 함수 사용하지 않은 코드
def sum(x, y):
    return x+y

target = list(range(1, 21)) # 1~20 정수 반환
result = 0
for value in target:
    result = sum(result, value)
print(result)

# reduce 함수 사용
from functools import reduce
def sum(x, y):
    return x+y
target = list(range(1, 21))
print(reduce(sum, target))

# reduce 함수 + lambda 표현
print(reduce(lambda x, y : x+y, target)) # reduce함수는 '누적', map함수는 list로 각 항목을 모아서 반환

