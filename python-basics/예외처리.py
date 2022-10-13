"""
예외처리
"""

try:
    4/0

#except 발생 오류 as 오류 메시지 변수
except ZeroDivisionError as e:
    print(e)

# try:
#     # run somethign
# finally: # 예외 발생 여부와 상관없이 무조건 실행하는 절
#     print("무조건 실행됨")


# try 문 안에서 여러 개의 오류를 처리하기 위한 구문
try:
    a = [1, 2]
    print(a[3])
    4/0

# 해당 오류는 indexError를 먼저 발생시키므로 ZeroDivisionError는 발생하지 않는다.
# 즉 먼저 발생하는 오류에 따른 구문만 실행된다.
except ZeroDivisionError as e: # 첫 번째 오류
    print("0으로 나눌 수 없다")
    print(e)
except IndexError as e: # 두 번째 오류
    print("인덱싱 할 수 없다")
    print(e)


# try:
#     # 수행할 구문
# except 예외:
#
# else: # 오류가 없을 경우에만 수행.
#       # finally 는 오류 여부에 관계없이 무조건 실행

# 예외 만들기
class MyCustomError(Exception):
    def __str__(self):
        return "내가 만든 예외 메시지"
    print("내가 만든 예외")



def say_nick(nick):
    if nick == '바보':
        raise MyCustomError
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyCustomError as e:
    print("내 에러")
    print(e)
