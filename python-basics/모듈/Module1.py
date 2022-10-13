def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# 다른 파일에서 이 모듈을 불러올 경우 아래 범위에 해당하는 명령어는 skip된다
# __name__ 변수는 파이썬이 내부적으로 사용하는 변수 이름이다.
if __name__ == "__main__":
    print(add(60, 3))
    print(sub(60, 3))