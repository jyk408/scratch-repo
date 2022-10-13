"""
숫자형
"""
# 나머지를 반환하는 연산자
print(7 % 3) # 3으로 7을 두 번 나눈 후 1이 남

# 나눗셈 후 몫을 반환
print(7 // 4) # 4로 7을 한 번 나누기 가능

# 나눗셈 후 몫을 반환 (소수점 단위 포함)
print(7 / 4) # 4로 7을 1.75번 나누기 가능

"""
문자열 자료형
"""

# 문자열에 따옴표(") 포함 시키기
print("Python \"s favorite food")

# 문자열 줄 바꾸기
print("Life is too short \nYou need Python")
print('''
Life is too short
You need Python''')

# 문자열 더하기
head = "Python"
tail = " is fun"
print(head + tail)

# 문자열 곱하기
temp = "python "
print(temp * 3)

# 문자열 길이
print(len("Python"))

# 문자열 인덱싱(무엇인가 가리킨다)과 슬라이싱(무엇인가를 잘라낸다)
temp = "Life is too short, you need Python"
print(temp[3])
print(temp[-1]) # 문자열 마지막 문자
print(temp[-2])

print(temp[0:3]) # 0 <= x < 3 이기때문에 시작문자 포함하고 마지막 문자는 제외한다.
print(temp[19:]) # 19 <= x <= 문자열마지막까지 포함시켜 반환
print(temp[:]) # 처음부터 끝까지 출력

# 문자열 포매팅
temp = "apple"
print("I love %d" % 3) # 숫자 바로 대입
print("I love %s" % temp) # 문자열 바로 대입
print("I love %f" % 4.44) # 소수 대입
print("I love %s and %s" % (temp, "banana")) # 두 개 대입
print("%10s" % "python") # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞에 나머지는 공백으로 채운다.
print("%-10s" % "python") # 전체길이 10개 문자열에서 대입값을 왼쪽으로 정렬 후 공백채운다
print("%0.4f" % 3.412351) # 소수점 네 번째 자리까지만 나타내고 싶을 경우
print("%10.4f" % 3.412351) # 전체 길이 10개인 문자열 공간에서 대입값을 오른쪽에 채우고 나머지는 공백으로 채운다. 또한 소수점을 4번째 자리까지만 표출

# format 함수를 이용한 포매팅
print("I love {0} and {1}".format("apple", "banana"))
print("I love {first} and {second}".format(second="banana", first="apple")) # 이름 인자값으로 넣기

# 문자열 관련 함수
temp = " i love python "
print(temp.count("p")) # 문자열에서 찾고싶은 문자 개수 세기
print(temp.find("p")) # 문자열에서 해당 문자 인덱스 위치 반환
                      # 문자가 있으면 index반환, 없으면 -1반환  (오류 발생 X)
print(temp.index("p")) # 인덱스 위치 반환
                       # 문자가 있으면 인덱스 반환, 없으면 오류 발생
print(",".join("abcd")) # abcd 문자열의 각각의 문자 사이에 콤마(,)를 삽입
print(temp.upper()) # 대문자로 변환
print(temp.lower()) # 소문자로 변환
print(temp.rstrip()) # 오른쪽 공백 지우기
print(temp.lstrip()) # 왼쪽 공백 지우기
print(temp.strip()) # 양 공백 지우기
print(temp.replace("python", "java")) # replace(바뀌게될 문자열, 바꿀 문자열) 값 치환
print(temp.split()) # 문자열을 공백기준으로 나누어 리스트로 변환해 반환

"""
리스트 자료형
"""

# 리스트 슬라이싱
temp = [1,2, 3, ["a", "b", "c"]]
print(temp[0])
print(temp[3]) # 리스트 안에 세부 리스트 전체 출력
print(temp[3][2]) # 리스트 안에 세부 리스트 2번째 인덱스 해당 문자 반환

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a)) # 리스트 안에 항목 개수  구하기
print(str(a[0]) + "python") # 리스트와 문자열 더하는 방법
a[2] = 4 # 리스트 값 수정
print(a)
del a[1:] # del함수를 이용한 리스트 요소 삭제
print(a)

# 리스트 관련 함수
a.append(2) # 리스트의 맨 마지막에 x를 추가하는 함수
a.append([3, 4]) # 리스트 안에는 어떤 자료형도 추가할 수 있다
print(a)
a = [1, 4, 3, 2]
a.sort() # 오름차순으로 정렬
print(a)
a.reverse() # 역순으로 뒤집어준다.
print(a)
a.index(3) # 해당 요소 값의 인덱스 값을 반환
           # 값이 존재 시 인덱스값 반환, 값이 없으면 에러 발생
a.insert(0, 4) # (a,b) a번째 인덱스 위치에 b값을 입력한다
a.remove(3)
a = [1, 2, 3]
print(a.pop(1)) # 리스트 1번째 인덱스의 해당하는 요소를 반환하고 그 요소는 삭제
print(a)
# count(x)는 문자열안에 x개수 세기, len(x)는 x리스트안에 총 요소 개수 세기
print(a.count(1)) # 리스트의 요소 개수 세기
a = [1,2,3]
a.extend([4,5,6]) # extend 함수에는 리스트만 사용가능
                  # a리스트에 x리스트를 더한다
print(a)

"""
튜플 자료형
  - 튜플은 몇 가지 점을 제외하곤 리스트와 거의 비슷하지만 다음과 같은 다른점이 있다.
  - 리스트는 []로 둘러싸지만 튜플은 ()로 둘러싼다
  - 리스트는 값을 수정할 수 있지만 튜플은 값을 수정할 수 없다.
  - 즉, 프로그램 실행 중 값이 항상 변하지 않기를 원하거나 값이 바뀔까 걱정되면 튜플을 사용
  - 프로그램에서 값이 수시로 변경되어야 한다면 리스트 사용
"""

# 튜플 생성
t1 = () # 빈 튜플 생성
t2 = (1,) # 1개의 요소만 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 괄호를 생략해도 무방
t5 = ("a", "b", ("c", "d"))

# 튜플 관련함수는 리스트와 같으므로 패스

"""
딕셔너리 자료형
"""

# 딕셔너리 쌍 추가, 삭제
a = {1: "a"}
a[2] ="b" # 리스트나 튜플같은 sequential 항목에서는 indexOutOfRange 에러가 발생
print(a)

del a[1] # del [key]
print(a)

# 딕셔너리 key를 이용해 value 가져오기
print(a[2])

# 딕셔너리 생성 시 주의사항
a = {1: 'a', 1:'b'} # key는 고유값이므로 중복되는 key값 설정시 하나는 무시된다.
                    # 또한 Key에는 리스트타입 사용이 불가하다

# 딕셔너리 관련 함수
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys()) # 딕셔너리 a의 key값을 모아 dict_keys객체에 돌려준다.
                # 파이썬 3.0 이전에는 list로 반환했지만 메모리 낭비가 발생하기에 python 3.0부터는 dict_keys객체를 돌려준다

# dictionary key값으로 반복문 돌리기
for key in a.keys():
    print(key)

# dictionary -> list로 변환
print(list(a.keys()))

# value 리스트 만들기
print(list(a.values()))

# 딕셔너리 key,value 쌍 얻기 (items)
print(a.items())
print(list(a.items()))

# key,value 모두 삭제
# a.clear()

# key로 value 가져오기
print(a.get('name'))

# dictionary.get() VS dictionary[key]
# dictionary의 get함수는 키값이 없을 경우 None 반환
# dictionary를 인덱스로 value를 가져올 경우 값이 없으면 error발생

# key가 딕셔너리 안에 있는지 조사 (in)
print('name' in a)



"""
집합 자료형
특징
  - 중복 허용 X
  - 순서가 없다 (unordered) 
  
리스트랑 튜플은 순서(ordered)가 있기때문에 indexing을 통해 값을 얻을 수 있지만
set은 순서가 없기 때문에 인덱싱 사용이 불가능. 
"""

# 집합 생성
s1 = set([1,2,3]) # set함수에 리스트[]를 입력
print(s1)
s2 = set("Hello") # set함수에 문자열을 입력
print(s2)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2) # 기호 사용
print(s1.intersection(s2)) # intersection 함수 사용

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 집합 관련 함수
# 이미 만들어진 set자료형에 값 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 동시에 추가 (중복값은 자동으로 제거)
s1.update([1, 2, 3, 4, 5, 6])
print(s1)

# 값 제거
s1.remove(2) # value값으로 제거 (index 아님!!)
print(s1)


"""
bool 자료형

문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 false
값이 존재하면 true
"""
print(bool("Python"))
print(bool([1,2]))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(1))
print(bool(0))


"""
변수
"""
a = [1,2,3]
b = a
# 변수가 가르키는 메모리 주소 반환
print(id(a))

# 두 변수가 가리키는 객체(메모리주소)는 동일한가
print(a is b)

