"""
클래스

객체와 인스턴스의 차이:
a = Cookie() 이렇게 만든 a는 객체이다
                      a 객체는 Cookie의 인스턴스이다.
즉, 인스턴스는 특정 객체a가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명
a는 인스턴스 X -> a는 객체
a는 Cookie의 객체 X -> a는 Cookie의 인스턴스
"""

class FourCal:
    # self 매개변수는 관례적으로 사용되며, 객체를 호출시 호출한 객체 자신이 전달되는 매개변수이다.
    # self 가 아닌 다른이름으로 지어도 작동은 하지만 관례를 따르도록 하자...
    # 파이썬만의 독특한 특징이다.
    def setData(self, a, b):
        self.a = a # 메소드 호출 시 전달한 인자값 a를 객체호출한 객체 자신인 cal1 or cal2의 a속성에 값 선어
        self.b = b # 다음과 같이도 해석된다. cal1객체가 메소드 호출 시 cal1.b = b로 볼 수 있다.

# 메소드 호출 방법 (객체이름.메소드) - self매개변수에 객체 전달 생략 가능
cal1 = FourCal()
cal1.setData(4, 2)

# 메소드의 또 다른 호출 방법 (클래스이름.메소드)
cal2 = FourCal()
FourCal.setData(cal2, 4, 2) # 이와 같이 클래스이름.메소드 형태로 호출할 때는 객체 cal2를 첫 번째 매개변수 self에 꼭 전달해야 한다.


"""
생성자 (constructor): 객체가 생성될 때 자동으로 호출되는 메소드
"""

class Student:

    def __init__(self, name):
        self.name = name

    def sayMyName(self):
        print(self.name)

"""
상속(inheritance): 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 함
"""

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class MoreCalculator(Calculator):

    # 메소드 오버라이딩
    def sub(self):
        print("오버라이딩 sub메소드 a에서 a를 뺀다")
        return self.a - self.a

# Calculator 부모 클래스의 __init__ 사용
a = MoreCalculator(2, 2)
print(a.add())
print(a.sub())
print(a.sub())
