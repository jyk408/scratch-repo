"""
Dataset: 샘플과 정답(label)을 저장

DataLoader: dataset을 샘플에 접근할 수 있또록 iterable(순회가능한)객체로 감싼다
"""

import torch
from torch.utils.data import dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

# 데이터셋 불러오기
training_data = datasets.FashionMNIST(
    root="data", # 학습/테스트 데이터가 저장되는 경로
    train=True, # 학습/테스트 데이터셋 여부를 선택
    download=True, # root에 데이터셋이 없는 경우 다운로드
    transform=ToTensor() # 특징(feature)과 정답(label) 변형(transform)을 지정
)

test_data = datasets.FashionMNIST(
    root="data", # 학습/테스트 데이터가 저장되는 경로
    train=False, # 학습/테스트 데이터셋 여부를 선택
    download=True, # root에 데이터셋이 없는 경우 다운로드
    transform=ToTensor() # 특징(feature)과 정답(label) 변형(transform)을 지정
)

# 데이터셋을 순회(iterate)하고 시각화하기
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8, 8)) # 8x8사이즈의 이미지 시각화
cols, rows = 3, 3 # figure를 세로로 3개 가로로 3개 총 9개 표출
for i in range(1, cols*rows + 1): # figure 9개 표출
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    image, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.imshow(image.squeeze(), cmap="gray")
plt.show()