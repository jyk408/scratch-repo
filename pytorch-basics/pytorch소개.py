"""
Pytorch Tensors
"""

import torch

z = torch.ones(5, 3)
print(z)
print(z.dtype)

torch.manual_seed(1729)
r1 = torch.rand(2,2)
print(r1)

r2 = torch.rand(2,2)
print("\n 다른 랜덤 텐서값: ")
print(r2)

torch.manual_seed(1729)
r3 = torch.rand(2,2)
print(r3) # 동일한 시드값으로 인해 r1값이 반복되어 행렬값으로 반환

ones = torch.ones(2,3)
twos = torch.ones(2,3) * 2 # 모든 원소에 2를 곱한다
three = ones + twos # 각 행렬의 shape이 같기에 연산수행 가능
                    # 다른 차원의 행렬을 연산 시 runtime 오류 발생
print(three)
print(three.shape)

r = (torch.rand(2,2) - 0.5) * 2 # -1과 1사이의 값을 가짇나
print('랜덤 행렬값, r:')
print(r)

# 일반적인 수학적 연산은 다음과 같이 지원됩니다:
print('\nr의 절대값:')
print(torch.abs(r))

# 삼각함수를 사용할 수 있습니다:
print('\nr의 역 사인 함수:')
print(torch.asin(r))

# 행렬식 및 특이값 분해와 같은 선형 대수 연산을 사용할 수 있습니다.
print('\nr의 행렬식:')
print(torch.det(r))
print('\nr의 특이값 분해:')
print(torch.svd(r))

# 통계 및 집합 연산 등을 사용할 수 있습니다:
print('\nr의 평균 및 표준편차:')
print(torch.std_mean(r))
print('\nr의 최대값:')
print(torch.max(r))


"""
pytorch models
"""
import torch # Pytorch 모든 모듈 가져오기
import torch.nn as nn # torch.nn.Module의 경우 Pytorch model의 부모 객체
import torch.nn.functional as F # 활성화(activation) 함수 가져오기

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        # 입력 이미지 채널, 6개의 output 채널, 3x3 정방 합성곱 커널을 사용
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)
