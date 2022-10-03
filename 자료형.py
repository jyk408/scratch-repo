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
