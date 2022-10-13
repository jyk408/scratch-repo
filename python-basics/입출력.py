"""
함수
"""

# 매개변수(parameter)와 인수(argument)
# 매개변수: 함수에 입력으로 전달된 값을 받는 변수
# 인수: 함수를 호출할 때 전달하는 입력값
# parameter==변수  argument==입력값
def add(a, b): # a, b는 매개변수(parameter)
    return a+b

print(add(1, 100)) # 1, 100은 인자(argument)

print(add(b=100, a=1)) # 매개변수를 지정하여 함수 호출

# 입력값이 몇개인지 정해지지 않았을 경우
def add(*coin_types): # 튜플 자료형으로 매개변수를 입력받는다
    print(type(coin_types))
    for coin in coin_types:
        print(coin)

print(add(500, 100, 50, 10))

# 키워드 파라미터 kwargs (an acronym for keyword arguments)
def print_fruit_and_price(**kwargs):
    print(type(kwargs)) # keyword arguments는 딕셔너리 타입으로 매개변수를 받는다
    for key, value in kwargs.items():
        print(key, value)

print_fruit_and_price(banana=10, apple=20, mango=300)

# 매개변수(parameter) 초기값 미리 설정
def say_name(name, man=True):
    if man:
        print("남자임")
    else:
        print("여자임")

print(say_name("william"))
print(say_name("william", False))

# lambda: 함수를 간결히 만들 때 사용
# syntax: lambda 매개변수1, 매개변수2, ...: 매개변수를 이용한 표현식
add = lambda x, y: x+y
print(add(1, 100))


"""
사용자 입력과 출력
"""

# 사용자 입력
# a = input("입력하세요: ")
# print(a)
# input에 입력되는 모든것은 "문자열"로 취급한다
# print(type(a))

# print함수에서 큰따옴표(")로 둘러쌓인 문자열은 + 연산과 동일하다
print("i" "love" "python")
print("i"+"love"+"python")

# 문자열 띄어쓰기는 콤마(,)로 한다
print("i", "love", "python")

"""
파일 읽고 쓰기
"""
# temp.txt라는 파일 생성
file = open("temp.txt", 'w') # open(파일이름, 파일 열기 모드)
                             # open("temp", 'r') 파일을 읽기만 할 때 사용
                             # open("temp", 'w') 파일에 내용을 쓸 때 사용
                                # 파일이 있으면 기존 내용 모두 삭제
                                # 파일이 없으면 새로 파일 생성
                             # open("temp", 'a') 파일의 마지막에 새로운 내용 추가시킬 때 사용
for i in range(1, 11):
    file.write("{} 번째 줄입니다 \n".format(i))
file.close()

# 외부 파일 읽기
file = open("temp.txt", 'r')
line = file.readline() # 파일의 첫 번째 줄을 읽는다.
print(line)
file.close()

# 외부 파일의 모든 줄을 읽기 (방법1)
file = open("temp.txt", 'r')
while True:
    line = file.readline()
    # 더이상 읽을 줄이 없을 경우 빈 문자열("")을 반납하기에 false반환됨
    if not line: break
    print(line)
print(file.readline())
file.close()

# 외부 파일의 모든 줄을 읽기 (방법2)
file = open("temp.txt", 'r')
# readlines는 각각의 줄을 줄바꿈(\n)문자 포함하여 반환한다.
for line in file.readlines():
    print(line)
file.close()

# readlines사용 시 줄바꿈 제거
file = open("temp.txt", 'r')
for line in file.readlines():
    print(line.strip())
print(type(file.readlines()))
file.close()

# 외부 파일의 모든 줄을 읽기 (방법3)
file = open("temp.txt", 'r')
# read()는 내용 전체를 문자열로 반환한다.
lines = file.read()
print(lines)
print(type(lines))
file.close()


# 파일에 새로운 내용 추가
file = open("temp.txt", 'a')
file.write("새로운 내용")
file.close()

# 파일 자동으로 열고 닫게 처리
with open("temp.txt", "w") as file: # 이 범위를 나가면 file이 자동으로 close()된다
    file.write("마지막 파일 수정")


# sys 모듈로 매개변수 주기
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# 사용 예시
# 입출력.py  apple   banana  mango
# argv[0]  argv[1] argv[2] argv[3]