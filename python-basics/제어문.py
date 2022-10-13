"""
if 문
"""

# 값을 비교하는 연산자
# <, >, ==, !=, >=, <=

# 조건을 비교하는 연산자
# x or y: x와 y중 하나만 true여도 true
# x and y: x 와 y 둘 다 true여야 true
# not x: x가 false 일경우 true

# x가 리스트 안에 있는지 판단
print(1 in [1,2,3])

# x가 튜플 안에 있는지 판단
print(1 in (1, 2, 3))

# x가 문자열 안에 있는지 판단
print('ba' in 'banana')

# 조건문에서 아무 일도 하지 않게 설정
a = [1, 2, 3]
if 1 in a:
    pass
else:
    print(1)


"""
while 문
"""

# while문의 맨 처음으로 돌아가기 (다음 loop으로 돌아가기)
a = 0
while a < 10:
    a += 1
    if  a % 2 ==0: continue # 짝수일 경우 다음 loop으로 돌아가기
    print(a)


"""
for 문
"""

# 전형적인 for 문
fruit = ["apple", "banana", "mango"]
for i in fruit:
    print(i)

# 다양한 for문
fruit_price = [("banana", 1), ("apple", 20),  ("mango", 300)]
for fruit, price in fruit_price:
    if fruit == "banana":
        continue
    print(fruit, price)

# for문과 자주 사용하는 range함수
for num in range(1, 11): # (x(포함),y(미포함))라 가정하에 x <= num < 11이다
    print(num, end=" ") # 매개변수 end는 결과값을 다음줄로 넘기지 않고 그 줄에 계속하게 출력을 위함
