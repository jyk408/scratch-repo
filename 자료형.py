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

