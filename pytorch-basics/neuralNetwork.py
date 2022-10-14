import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# GPU에서 학습 설정
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


# neuralnetwork 모델 생성 후 device에 이동 후 모델 구조 (structure) 출력
model = NeuralNetwork().to(device)
print(model)

input_image = torch.rand(3, 28, 28) # 28x28 크기의 이미지 3개
print(input_image.size())
flatten = nn.Flatten()
flat_image = flatten(input_image) # 28x28사이즈 이미지를 1차원 데이터로 압축
print(flat_image.size())

# nn.Linear: 선형 계층은 가중치(weight)와 편향(bias)를 사용하여 입력에 선형변형(linear transformation)을 적용하는 모듈
## linear transformation: y=wx+b
layer1 = nn.Linear(in_features=28*28, out_features=20)
hidden1 = layer1(flat_image)
print(hidden1.size())

# nn.Sequential: 순서를 갖는 모듈의 컨테이너. 입력값은 정의된 것과 같은 순서대로 데이터가 전달된다.
sequential_model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(in_features=28*28, out_features=20),
    nn.ReLU(),
    nn.Linear(in_features=20, out_features=10)
)
input_image = torch.rand(3, 28, 28)
logits = sequential_model(input_image)
print(logits)

# nn.Softmax: 모델의 각 분류(class)에 대한 예측을 [0,1] 범위로 비례해 조정(scale)
## dim 파라미터(매개변수)는 값의 합이 1이 되는 차원
softmax = nn.Softmax(dim=1)
predict_probability = softmax(logits)
print(predict_probability)

# 모델 매개변수
for name, param in model.named_parameters():
    print(f"Layer: {name} | Size:0 {param.size()} | value: {param[:2]}\n")