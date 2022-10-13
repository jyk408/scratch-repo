""""
모듈: 함수나 변수 또는 클래스를 모아둔 파일.
     다른 파이썬 파일에서 불러와 사용하는 용도
"""

# import [모듈이름]
import Module1
print(Module1.add(4, 2))

# from [모듈이름] import [모듈함수]
from Module1 import sub # 모듈 함수를 바로 사용하기 위함
print(sub(8, 3))

# 모듈2
import Module2
print(Module2.PI)

math = Module2.Math()
print(math.solv(5))

# 모듈을 불러오는 또 다른 방법
# sys.path.append(모듈을 저장한 디렉토리) 활용
import sys
sys.path.append("/Users/william/PycharmProjects/python-basics/모듈")
print(sys.path)